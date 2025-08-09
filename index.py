
from data_processing import clean_data, unscale_thetas
from gradient_descent import gradient_descent, hypothesis


def white_to_red_gradient(n):
    if n <= 0:
        colors = []
        for i in range(n):
            t = i / (n - 1)  # t goes from 0 to 1
            r = 255
            g = int(255 * (1 - t))
            b = int(255 * (1 - t))
            hex_color = f'#{r:02x}{g:02x}{b:02x}'
            colors.append(hex_color)
        return colors
    return [f'#{255:02x}{0:02x}{0:02x}']

def save_results(plot, theta0, theta1, output_dir):
    import os
    import csv
    os.makedirs(output_dir, exist_ok=True)
    plot.savefig(f'{output_dir}/plot.png')
    with open(f'{output_dir}/results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['theta0', 'theta1'])
        writer.writerow([theta0, theta1])

def plot(
        X,
        x_name,
        y,
        y_name,
        output_dir,
        steps,
        amount_lines,
        alpha,
):
    red_colors = white_to_red_gradient(amount_lines)
    
    X_filtered, y_filtered, X_scaled, y_scaled, x_min, x_max, y_min, y_max = clean_data(X, y)

    import matplotlib.pyplot as plt
    plt.scatter(X_filtered, y_filtered, color='blue', label='Data')
    theta0_scaled, theta1_scaled = gradient_descent(X_scaled, y_scaled, alpha=alpha, steps=steps, 
        printStep=True,
        condition_step_func=lambda step: step != 0 and step % (steps/amount_lines) == 0, 
        on_condition_step_func=lambda step, t0, t1: plt.plot(X, [hypothesis(t0, t1, xi) for xi in X], color=red_colors[round(step/steps * amount_lines)], label=f'Step {step}')
        )
    theta0_unscaled, theta1_unscaled = unscale_thetas(theta0_scaled, theta1_scaled, x_min, x_max, y_min, y_max)
    plt.plot(X_filtered, [hypothesis(theta0_unscaled, theta1_unscaled, xi) for xi in X_filtered], color='red', label='Best fit line')
    plt.legend()
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title('Linear Regression with Gradient Descent')
    plt.grid(True)
    save_results(plt, theta0_unscaled, theta1_unscaled, output_dir)
    plt.show()

def main():
    DEFAULT_STEPS = 3_000
    DEFAULT_AMOUNT_LINES = 1
    DEFAULT_FILENAME = 'data/properties.csv'
    DEFAULT_ALPHA = 0.3
    DEFAULT_X = 'area'
    DEFAULT_Y = 'price'
    DEFAULT_OUTPUT = 'results/YYYY-MM-DD HH:MM:SS/'

    import argparse
    parser = argparse.ArgumentParser(description='Run gradient descent for linear regression.')
    parser.add_argument('--steps', 
                        type=int, 
                        default=DEFAULT_STEPS, 
                        help='Number of steps for gradient descent (default: {DEFAULT_STEPS})')
    parser.add_argument('--filename', 
                        type=str,
                        default=DEFAULT_FILENAME, 
                        help=f'Filename containing the data. Must be in CSV format. Required.')
    parser.add_argument('--amount-lines', 
                        type=int, 
                        default=DEFAULT_AMOUNT_LINES, 
                        help=f'Number of lines to plot during gradient descent (default: {DEFAULT_AMOUNT_LINES})')
    parser.add_argument('--x', 
                        type=str,
                        default=DEFAULT_X, 
                        help=f'Column name for x values in the CSV file (default: {DEFAULT_X})')
    parser.add_argument('--y', 
                        type=str,
                        default=DEFAULT_Y, help=f'Column name for y values in the CSV file (default: {DEFAULT_Y})')
    parser.add_argument('--alpha', 
                        default=DEFAULT_ALPHA, 
                        help=f'Learning rate for gradient descent (default: {DEFAULT_ALPHA})')
    parser.add_argument('--output',
                        help=f'Output directory for results. Defaults to "results" with a timestamp folder (default: {DEFAULT_OUTPUT})')
    args = parser.parse_args()

    output_dir = args.output
    if not output_dir:
        from datetime import datetime
        timestamp = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        output_dir = f'results/{timestamp}'
        
    import pandas as pd
    data = pd.read_csv(args.filename)
    if args.x not in data.columns or args.y not in data.columns:
        print(f"Columns '{args.x}' and '{args.y}' must exist in the CSV file.")
        return
    X = data[args.x].tolist()
    y = data[args.y].tolist()
    x_name = args.x
    y_name = args.y

    plot(X, x_name, y, y_name, output_dir, steps=args.steps, amount_lines=args.amount_lines, alpha=args.alpha)

if __name__ == '__main__':
    main()