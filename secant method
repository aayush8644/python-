import numpy as np
import matplotlib.pyplot as plt

# Function definition
def f(x):
    return x**3 - x - 1


# Secant Method
def secant_method(f, x0, x1, tol, max_iter):
    iterations = []
    errors = []

    print("\nIter\t x_n\t\t f(x_n)\t\t Absolute Error")
    print("------------------------------------------------")

    for i in range(1, max_iter + 1):

        if f(x1) - f(x0) == 0:
            print("Division by zero encountered. Method fails.")
            return None, iterations, errors

        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        abs_error = abs(x2 - x1)

        iterations.append(i)
        errors.append(abs_error)

        print(f"{i}\t{x2:.6f}\t {f(x2):.6f}\t{abs_error:.6f}")

        if abs_error < tol:
            print("\nConverged successfully")
            return x2, iterations, errors

        x0, x1 = x1, x2

    print("\nMethod did not converge within given iterations")
    return x2, iterations, errors


# -------- Input Section --------
while True:
    try:
        x0, x1 = map(float, input("Enter initial guesses x0 and x1: ").split())
        if x0 == x1:
            print("Initial guesses must be different.")
            continue
        break
    except ValueError:
        print("Enter two numeric values.")

while True:
    try:
        tol = float(input("Enter absolute error tolerance: "))
        if tol <= 0:
            print("Tolerance must be positive.")
            continue
        break
    except ValueError:
        print("Enter a numeric value.")

while True:
    try:
        max_iter = int(input("Enter maximum number of iterations: "))
        if max_iter <= 0:
            print("Iterations must be positive.")
            continue
        break
    except ValueError:
        print("Enter a numeric value.")


# -------- Execution --------
root, iterations, errors = secant_method(f, x0, x1, tol, max_iter)


# -------- Plotting --------
if root is not None:
    x_vals = np.linspace(root - 2, root + 2, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(12, 5))

    # Function Plot
    plt.subplot(1, 2, 1)
    plt.axhline(0)
    plt.plot(x_vals, y_vals)
    plt.plot(root, f(root), 'ro')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Function Plot (Secant Method)")

    # Error Convergence Plot
    plt.subplot(1, 2, 2)
    plt.plot(iterations, errors, marker='o')
    plt.xlabel("Iteration")
    plt.ylabel("Absolute Error")
    plt.title("Error Convergence")

    plt.tight_layout()
    plt.show()
