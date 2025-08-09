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
    X,                              # Input features
    y,                              # Target variable
    alpha=0.01,                     # Learning rate
    steps=1000,                     # Number of iterations

    printStep=False,                # Whether to print the cost at each step
    condition_step_func=None,       # Optional function to call at each step
    on_condition_step_func=None,    # Function to call when condition_step_func returns true
):
    """
    Perform gradient descent to find the best fitting line for linear regression.

    Args:
    X: Input features
    y:  Target variable
    alpha:  Learning rate
    steps:  Number of iterations
    printStep: Whether to print information for each step.
    condition_step_func: Optional function to call at each step. Callback with step number as first parameter.
    on_condition_step_func: Function to call when condition_step_func returns true. Callback with step, theta 0 and theta 1 as parameters.
    """
    if len(X) != len(y):
        print("The length of x and y must be the same.")
        return

    theta0 = 0.0
    theta1 = 0.0
    m = len(X)

    for step in range(steps):
        theta0, theta1 = gradient_descent_step(X, y, m, (theta0, theta1), alpha)
        predictions = [hypothesis(theta0, theta1, xi) for xi in X]

        if printStep:
            cost = cost_function(y, predictions, m)
            print(f"Step {step}: Cost = {cost}, Theta0 = {theta0}, Theta1 = {theta1}")

        if condition_step_func is not None:
            if condition_step_func(step):
                if on_condition_step_func is not None:
                    on_condition_step_func(step, theta0, theta1)

    return theta0, theta1
