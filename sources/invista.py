import math
import requests
from typing import Iterator

from utils.formatter import formatAreaAsNumber, formatMoneyAsNumber, replaceAccents, replaceSpacesWithUnderscores
from utils.model import Property

PRINT_PREFIX = 'Invista: '
def logProgress(message: str) -> None:
    """
    Logs a message with the Invista prefix.
    """
    print(f"{PRINT_PREFIX}{message}")

def getProperties() -> Iterator[list[Property]]:
    """
    Generator that yields Property objects from the Invista website one at a time.
    """
    properties, total = getPropertiesInPage(1)
    total_pages = math.ceil(total / 20)
    yield properties
    for page in range(2, total_pages + 1):
        page_properties, _ = getPropertiesInPage(page)
        yield page_properties
        progress = round((page * 20) / total * 100, 2)
        logProgress(f'{progress}% - Page {page} out of {total_pages}.')
    logProgress(f'Finished fetching {total} properties.')


def getPropertiesList() -> list[Property]:
    """
    Returns a list of Property objects from the Invista website (eager, not generator).
    """
    properties, total = getPropertiesInPage(1)
    total_pages = math.ceil(total / 20)
    for page in range(2, total_pages + 1):
        page_properties, _ = getPropertiesInPage(page)
        properties.extend(page_properties)
        progress = round(len(properties) / total * 100, 2)
        logProgress(f'{progress}% - Page {page} out of {total_pages}.')
    logProgress(f'Finished fetching {len(properties)} properties.')
    return properties


def getPropertiesInPage(page: int) -> list[Property]:
    """
    Returns a list of Property objects for the given page.
    """
    properties = []
    url = 'https://www.invistaii.com.br/retornar-imoveis-disponiveis'
    form_data = f'finalidade=venda&codigounidade=&codigocondominio=0&codigoproprietario=0&codigocaptador=0&codigosimovei=0&codigocidade=0&codigoregiao=0&bairros%5B0%5D%5Bcidade%5D=&bairros%5B0%5D%5Bcodigo%5D=&bairros%5B0%5D%5Bestado%5D=&bairros%5B0%5D%5BestadoUrl%5D=&bairros%5B0%5D%5Bnome%5D=Todos&bairros%5B0%5D%5BnomeUrl%5D=todos-os-bairros&bairros%5B0%5D%5Bregiao%5D=&endereco=&edificio=&numeroquartos=0&numerovagas=0&numerobanhos=0&numerosuite=0&numerovaranda=0&numeroelevador=0&valorde=0&valorate=0&areade=0&areaate=0&areaexternade=0&areaexternaate=0&extras=&destaque=0&opcaoimovel=0&numeropagina={page}&numeroregistros=20&ordenacao=dataatualizacaodesc&condominio%5Bcodigo%5D=0&condominio%5Bnome%5D=&condominio%5BnomeUrl%5D=todos-os-condominios'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=form_data, headers=headers)
    json = response.json()
    for property in json['lista']:
        try:
            properties.append(Property(
                area=formatAreaAsNumber(property['areaprincipal']),
                neighborhood=replaceSpacesWithUnderscores(replaceAccents(property['bairro'].lower())),
                bedrooms=property['numeroquartos'],
                living_rooms=property['numerosalas'],
                bathrooms=property['numerobanhos'],
                parking_spaces=property['numerovagas'],
                property_type=replaceAccents(property['tipo'].lower()),
                price=formatMoneyAsNumber(property['valor']),
                source='invista'
            ))
            pass
        except Exception:
            continue
    return properties, json['quantidade']