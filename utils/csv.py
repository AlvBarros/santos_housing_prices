import os
import csv


from utils.model import Property


DEFAULT_DIR = 'data'
DEFAULT_FILENAME = 'properties.csv'
COLUMN_HEADERS = [
        'area',             # number in meters squared          - ex. 100.00
        'neighborhood',     # string                            - ex. 'Gonzaga'
        'bedrooms',         # number                            - ex. 2
        'living_rooms',     # number                            - ex. 1
        'bathrooms',        # number                            - ex. 1
        'parking_spaces',   # number                            - ex. 1
        'property_type',    # string                            - ex. 'apartment'
        'price',            # number with two decimal places    - ex. 500000.00
        'source'            # string                            - ex. 'Invista'
    ]

def clearOutputDir(output_dir: str, filename: str) -> None:
    """
    Clears the output directory by removing the properties.csv file if it exists.
    """
    output_file = os.path.join(output_dir, filename)
    if os.path.exists(output_file):
        os.remove(output_file)


def checkCSVHeaders(dir: str, filename: str) -> bool:
    """
    Checks if the CSV file exists and has the correct headers as the first row.
    Returns True if headers match, False otherwise.
    """
    output_file = os.path.join(dir, filename)
    if not os.path.exists(output_file):
        return False
    with open(output_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        try:
            first_row = next(reader)
        except StopIteration:
            return False
        return first_row == COLUMN_HEADERS

def writeCSVHeaders(output_dir: str, filename: str) -> None:
    """
    Writes only the header row to the CSV file in the specified output directory.
    Overwrites any existing file.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, filename)
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=COLUMN_HEADERS)
        writer.writeheader()

def writeProperties(output_dir: str, filename: str, properties: list[Property]) -> None:
    """
    Appends Property objects to a CSV file in the specified output directory.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, filename)
    with open(output_file, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=COLUMN_HEADERS)
        for prop in properties:
            writer.writerow(prop.toDictionary())