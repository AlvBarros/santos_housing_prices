import argparse
from utils.csv import DEFAULT_DIR, DEFAULT_FILENAME, checkCSVHeaders, clearOutputDir, writeCSVHeaders, writeProperties

def main():
    parser = argparse.ArgumentParser(description='Fetch and store property data from sources.')
    parser.add_argument('--clear', action='store_true', default=True, help='Clear the current database before fetching (default: True)')
    parser.add_argument('--sources', nargs='+', default=['invista', 'rodaimoveis'], help='List of sources to fetch from (default: ["invista"])')
    parser.add_argument('--output-dir', default=DEFAULT_DIR, help=f'Directory to store the output CSV (default: {DEFAULT_DIR})')
    parser.add_argument('--filename', default=DEFAULT_FILENAME, help=f'Filename for the output CSV (default: {DEFAULT_FILENAME})')
    args = parser.parse_args()

    if args.clear:
        clearOutputDir(args.output_dir, args.filename)
        writeCSVHeaders(args.output_dir, args.filename)
    else:
        hasHeaders = checkCSVHeaders(args.output_dir, args.filename)
        if not hasHeaders:
            print(f"CSV file not found or headers do not match. Please clear the directory or fix the headers in {args.output_dir}/{args.filename}.")
            return
    
    total_saved = 0
    if 'rodaimoveis' in args.sources:
        from sources.rodaimoveis import getProperties
        for propertiesList in getProperties():
            writeProperties(args.output_dir, args.filename, propertiesList)
            total_saved += len(propertiesList)
    if 'invista' in args.sources:
        from sources.invista import getProperties
        for propertiesList in getProperties():
            writeProperties(args.output_dir, args.filename, propertiesList)
            total_saved += len(propertiesList)
    print(f"Saved {total_saved} properties to {args.output_dir}/properties.csv")

if __name__ == '__main__':
    main()