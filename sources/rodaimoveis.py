import math
import requests
from typing import Iterator
import re
from bs4 import BeautifulSoup

# from utils.formatter import formatAreaAsNumber, formatMoneyAsNumber, replaceAccents, replaceSpacesWithUnderscores
# from utils.model import Property

# PRINT_PREFIX = 'RodaImoveis: '
# def logProgress(message: str) -> None:
#     """
#     Logs a message with the RodaImoveis prefix.
#     """
#     print(f"{PRINT_PREFIX}{message}")

# def getProperties() -> Iterator[list[Property]]:
#     """
#     Generator that yields Property objects from the RodaImoveis website one at a time.
#     """
#     properties, total = getPropertiesInPage(1)
#     total_pages = math.ceil(total / 20)
#     yield properties
#     for page in range(2, total_pages + 1):
#         page_properties, _ = getPropertiesInPage(page)
#         yield page_properties
#         progress = round((page * 20) / total * 100, 2)
#         logProgress(f'{progress}% - Page {page} out of {total_pages}.')
#     logProgress(f'Finished fetching {total} properties.')

# def getPropertiesList() -> list[Property]:
#     """
#     Returns a list of Property objects from the RodaImoveis website (eager, not generator).
#     """
#     properties, total = getPropertiesInPage(1)
#     total_pages = math.ceil(total / 20)
#     for page in range(2, total_pages + 1):
#         page_properties, _ = getPropertiesInPage(page)
#         properties.extend(page_properties)
#         progress = round(len(properties) / total * 100, 2)
#         logProgress(f'{progress}% - Page {page} out of {total_pages}.')
#     logProgress(f'Finished fetching {len(properties)} properties.')
#     return properties

def parse_properties_from_html_from_first_page(html: str) -> list[dict]:
    """
    Parses the HTML and extracts property data into a list of dictionaries using regex.
    Each dictionary contains keys: area, neighborhood, bedrooms, living_rooms, bathrooms, parking_spaces, property_type, price
    """
    properties = []
    soup = BeautifulSoup(html, 'html.parser')
    imovelBoxSingles = soup.find_all('div', {'class': 'imovel-box-single', 'data-codigo': True})
    for imovelBox in imovelBoxSingles:
        prop = {}
        divValores = imovelBox.find('div', {'class': 'div-valores'})
        if len(divValores) == 0:
            continue
        prop['price'] = divValores.find('span', {'itemprop': 'price'}).text.strip()

        amenitiesMain = imovelBox.find_all('div', {'class': 'amenities-main'})
        if len(amenitiesMain) == 0:
            amenitiesDivs = amenitiesMain[0].find_all('div')
            for amenityDiv in amenitiesDivs:
                amenityIcon = amenityDiv.find('i')
                if not amenityIcon:
                    continue
                iconClass = amenityIcon.get('class', [])
                if 'fa-bed' in iconClass:
                    prop['bedrooms'] = amenityDiv.find('span').text.strip()
                elif 'fa-car' in iconClass:
                    prop['parking_spaces'] = amenityDiv.find('span').text.strip()
                elif 'fa-compress-arrows-alt' in iconClass:
                    prop['area'] = amenityDiv.find('span').text.strip()

        address = imovelBox.find('h3', {'itemprop': 'streetAddress'})
        prop['neighborhood'] = address.text.strip().split(' ')[0].lower()
        
        prop['property_type'] = 'apartment'
        # properties.append(Property(
        #     area=formatAreaAsNumber(property['areaprincipal']),
        #     neighborhood=replaceSpacesWithUnderscores(replaceAccents(property['bairro'].lower())),
        #     bedrooms=property['numeroquartos'],
        #     living_rooms=property['numerosalas'],
        #     bathrooms=property['numerobanhos'],
        #     parking_spaces=property['numerovagas'],
        #     property_type=replaceAccents(property['tipo'].lower()),
        #     price=formatMoneyAsNumber(property['valor']),
        #     source='invista'
        # ))
        properties.append(prop)
    return properties

def getPropertiesInPage(page: int):
    session = requests.Session()
    # Step 1: Visit the main listing page to establish session/cookies
    main_url = 'https://rodaimoveis.com.br/venda/apartamento/santos/'
    session.get(main_url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:138.0) Gecko/20100101 Firefox/138.0'
    })
    # Step 2: Make the AJAX request with the same session
    url = f'https://rodaimoveis.com.br/u-sr.php?page={page}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:138.0) Gecko/20100101 Firefox/138.0',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': main_url
    }
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        html = response.text
        if page == 1:
            properties = parse_properties_from_html_from_first_page(html)
            return properties
        else:
            return None
    else:
        print(f"An error occurred: {response.status_code} {response.reason}")
        return None

props = getPropertiesInPage(1)
print(props)