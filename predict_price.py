def predict_house_price(area, result_file):
        theta0, theta1 = get_thetas_from_result(result_file)
        price = theta0 + theta1 * area
        return price

def get_thetas_from_result(result_file):
    import os
    import csv
    if not os.path.exists(result_file):
        print(f"Result file {result_file} does not exist.")
        return None, None
    
    with open(result_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        row = next(reader)
        return float(row[0]), float(row[1])

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Predict the price for a house based on its area.')
    parser.add_argument('--area', 
                        type=int, 
                        help='Area of the house')
    parser.add_argument('--result-file',
                        type=str, 
                        help='CSV file containing the results with theta0 and theta1')
    args = parser.parse_args()

    if not args.area:
        print("Please provide the area of the house using --area argument.")
        return
    if not args.result_file:
        print("Please provide the result file containing theta0 and theta1 using --result-file argument.")
        return
    
    theta0, theta1 = get_thetas_from_result(args.result_file)
    if theta0 is None or theta1 is None:
        print("Could not retrieve thetas from result file.")
        return None
    
    result = predict_house_price(args.area, args.result_file)
    print(result)
    return result
        
if __name__ == '__main__':
    main()