def remove_outliers(X, y, threshold=3.0):
    def z_scores(values):
        mean = sum(values) / len(values)
        std = (sum((v - mean) ** 2 for v in values) / len(values)) ** 0.5
        return [(v - mean) / std for v in values], mean, std

    x_z, x_mean, x_std = z_scores(X)
    y_z, y_mean, y_std = z_scores(y)

    filtered = [
        (xi, yi)
        for xi, zi_x, zi_y in zip(X, x_z, y_z)
        for yi in [y[X.index(xi)]]
        if abs(zi_x) <= threshold and abs(zi_y) <= threshold
    ]

    if not filtered:
        raise ValueError("All data removed as outliers!")

    X_filtered, y_filtered = zip(*filtered)
    
    return X_filtered, y_filtered

def minmax(X, y):
    x_min, x_max = min(X), max(X)
    y_min, y_max = min(y), max(y)

    X_scaled = [(xi - x_min) / (x_max - x_min) for xi in X]
    y_scaled = [(yi - y_min) / (y_max - y_min) for yi in y]

    return X_scaled, y_scaled, x_min, x_max, y_min, y_max

def unscale_thetas(theta0_scaled, theta1_scaled, x_min, x_max, y_min, y_max):
    """
    Unscale the thetas back to the original scale.
    This is necessary after performing gradient descent on scaled data.
    """
    x_range = x_max - x_min
    y_range = y_max - y_min

    theta1_unscaled = (y_range / x_range) * theta1_scaled
    theta0_unscaled = y_min + y_range * (theta0_scaled - theta1_scaled * (x_min / x_range))
    return theta0_unscaled, theta1_unscaled

def clean_data(X, y):
    """
    Process the data by removing outliers and scaling.
    Returns scaled X, scaled y, and the original min/max values for unscaling.
    """
    X_filtered, y_filtered = remove_outliers(X, y)
    X_scaled, y_scaled, x_min, x_max, y_min, y_max = minmax(X_filtered, y_filtered)
    return X_filtered, y_filtered, X_scaled, y_scaled, x_min, x_max, y_min, y_max