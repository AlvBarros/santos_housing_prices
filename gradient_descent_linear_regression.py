def hypothesis(
        theta0,
        theta1,
        x
):
    """
        Hypothesis function for linear regression.
        h(x) = theta0 + theta1 * x
    """
    return theta0 + theta1 * x

def cost_function(
    y,              # Target variable
    predictions,    # Model predictions
    m               # Number of training examples
):
    """
        Calculate the cost function for linear regression.
        J(theta) = (1/(2*m)) * sum(errors^2)
    """
    sumErrorsSquared = 0.0
    for i in range(m):
        sumErrorsSquared += (predictions[i] - y[i]) ** 2.0

    return (1.0 / (2.0 * m)) * sumErrorsSquared

def gradient_descent_step(
        X,          # Input features
        y,          # Target variable
        m,          # Number of training examples
        thetas,     # Tuple of (theta0, theta1)
        alpha       # Learning rate
):
    """
        Perform a single step of gradient descent.
        theta0 = theta0 - alpha * (1/m) * sum(errors)
        theta1 = theta1 - alpha * (1/m) * sum(errors * X)
    """
    theta0, theta1 = thetas

    sumHypothesisMinusValue = 0
    sumHypothesisMinusValueTimesX = 0
    for i in range(m):
        hypothesis_value = hypothesis(theta0, theta1, X[i])
        error = hypothesis_value - y[i]
        sumHypothesisMinusValue += error
        sumHypothesisMinusValueTimesX += error * X[i]
    
    theta0 = theta0 - (alpha * 1 / m) * sumHypothesisMinusValue
    theta1 = theta1 - (alpha * 1 / m) * sumHypothesisMinusValueTimesX

    return theta0, theta1


def gradient_descent(
    X,                          # Input features
    y,                          # Target variable
    alpha=0.01,                 # Learning rate
    steps=1000,                 # Number of iterations
    
    condition_step_func=None,    # Optional function to call at each step
    on_condition_step_func=None, # Function to call when condition_step_func returns true
):
    m = len(y) # Number of training examples
    theta0 = 0.0
    theta1 = 0.0

    for step in range(steps):
        # Perform a gradient descent step
        theta0, theta1 = gradient_descent_step(X, y, m, (theta0, theta1), alpha)

        # Calculate predictions
        predictions = [hypothesis(theta0, theta1, xi) for xi in X]

        # Calculate cost
        cost = cost_function(y, predictions, m)

        # if step % 100 == 0:  # Print cost every 100 steps
        print(f"Step {step}: Cost = {cost}, Theta0 = {theta0}, Theta1 = {theta1}")

        # Call the condition step function if provided
        if condition_step_func is not None:
            if condition_step_func(step):
                if on_condition_step_func is not None:
                    on_condition_step_func(step, theta0, theta1)
    
    return theta0, theta1

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

def plot(
        X,
        y,
        steps=1000,
        amount_lines=10,
        alpha=0.001
):
    red_colors = white_to_red_gradient(amount_lines)
    import matplotlib.pyplot as plt
    plt.scatter(X, y, color='blue', label='Data')
    theta0, theta1 = gradient_descent(X, y, alpha=alpha, steps=steps, 
        condition_step_func=lambda step: step != 0 and step % (steps/amount_lines) == 0, 
        on_condition_step_func=lambda step, t0, t1: plt.plot(X, [hypothesis(t0, t1, xi) for xi in X], color=red_colors[round(step/steps * amount_lines)], label=f'Step {step}')
        )
    plt.plot(X, [hypothesis(theta0, theta1, xi) for xi in X], color='red', label='Best fit line')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Regression with Gradient Descent')
    plt.grid(True)
    plt.show()

def remove_outliers_minmax(X, y, threshold=3.0):
    # Step 1: Remove outliers using z-score method
    def z_scores(values):
        mean = sum(values) / len(values)
        std = (sum((v - mean) ** 2 for v in values) / len(values)) ** 0.5
        return [(v - mean) / std for v in values], mean, std

    x_z, x_mean, x_std = z_scores(X)
    y_z, y_mean, y_std = z_scores(y)

    # Step 2: Filter points with |z| > threshold
    filtered = [
        (xi, yi)
        for xi, zi_x, zi_y in zip(X, x_z, y_z)
        for yi in [y[X.index(xi)]]
        if abs(zi_x) <= threshold and abs(zi_y) <= threshold
    ]

    if not filtered:
        raise ValueError("All data removed as outliers!")

    X_filtered, y_filtered = zip(*filtered)

    # Step 3: Apply Min-Max scaling
    x_min, x_max = min(X_filtered), max(X_filtered)
    y_min, y_max = min(y_filtered), max(y_filtered)

    X_scaled = [(xi - x_min) / (x_max - x_min) for xi in X_filtered]
    y_scaled = [(yi - y_min) / (y_max - y_min) for yi in y_filtered]

    return X_scaled, y_scaled, x_min, x_max, y_min, y_max


def main():
    DEFAULT_STEPS = 3_000
    DEFAULT_LEARNING_RATE = 0.3
    DEFAULT_AMOUNT_LINES = 1
    DEFAULT_X = 'area'
    DEFAULT_Y = 'price'
    import argparse
    parser = argparse.ArgumentParser(description='Run gradient descent for linear regression.')
    parser.add_argument('--steps', type=int, default=DEFAULT_STEPS, help='Number of steps for gradient descent (default: {DEFAULT_STEPS})')
    parser.add_argument('--amount-lines', type=int, default=DEFAULT_AMOUNT_LINES, help='Number of lines to plot during gradient descent (default: {DEFAULT_AMOUNT_LINES})')
    parser.add_argument('--filename', help=f'Filename containing the data. Must be in CSV format. Required.')
    parser.add_argument('--x', default='area', help=f'Column name for x values in the CSV file (default: {DEFAULT_X})')
    parser.add_argument('--y', default='price', help=f'Column name for y values in the CSV file (default: {DEFAULT_Y})')
    parser.add_argument('--alpha', default=0.3, help=f'Learning rate for gradient descent (default: {DEFAULT_LEARNING_RATE})')
    args = parser.parse_args()

    if not args.filename:
        print("Please provide a filename.")
        return

    import pandas as pd
    data = pd.read_csv(args.filename)
    if args.x not in data.columns or args.y not in data.columns:
        print(f"Columns '{args.x}' and '{args.y}' must exist in the CSV file.")
        return
    X = data[args.x].tolist()
    y = data[args.y].tolist()

    if len(X) != len(y):
        print("The length of x and y must be the same.")
        return
    
    X_scaled, y_scaled, x_min, x_max, y_min, y_max = remove_outliers_minmax(X, y)
    print(f"Data after removing outliers and scaling: {len(X_scaled)} points")
    print(f"x range: {x_min} to {x_max}, y range: {y_min} to {y_max}")

    plot(X_scaled, y_scaled, steps=args.steps, amount_lines=args.amount_lines, alpha=args.alpha)

if __name__ == '__main__':
    main()