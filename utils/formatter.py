def formatAreaAsNumber(area: str) -> float:
    """
    Converts an area string (e.g., '100,00') to a float (e.g., 100.00).
    """
    if not area or area == '0,00':
        return 0.0
    # Replace ',' with '.' and convert to float
    return float(area.replace(',', '.').strip())

def formatMoneyAsNumber(money: str) -> float:
    """
    Converts a money string (e.g., 'R$ 500.000,00') to a float (e.g., 500000.00).
    """
    if not money or money == 'R$ 0,00':
        return 0.0
    # Remove 'R$' and replace '.' with '' and ',' with '.'
    return float(money.replace('R$', '').replace('.', '').replace(',', '.').strip())

def replaceAccents(text: str) -> str:
    """
    Replaces accented characters in a string with their non-accented equivalents.
    """
    accents = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i',
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u',
        'ç': 'c'
    }
    for accented_char, non_accented_char in accents.items():
        text = text.replace(accented_char, non_accented_char)
    return text

def replaceSpacesWithUnderscores(text: str) -> str:
    """
    Replaces spaces in a string with underscores.
    """
    return text.replace(' ', '_')