import numpy as np
import matplotlib.pyplot as plt

# Newton-Raphson Method

def f(x):
    return x**3 - x - 1

def df(x):
    return 3*x**2 - 1

x = float(input("Enter initial guess x0: "))
tol = float(input("Enter absolute error tolerance: "))
max_iter = int(input("Enter maximum number of iterations: "))

errors = []
iterations = []

print("\nIter\t x_n\t\t f(x_n)\t\t Absolute Error")

for i in range(1, max_iter + 1):

    if df(x) == 0:
        print("Derivative is zero. Method fails.")
        break

    x_new = x - f(x)/df(x)
    abs_error = abs(x_new - x)

    errors.append(abs_error)
    iterations.append(i)

    print(f"{i}\t {x_new:.6f}\t {f(x_new):.6f}\t {abs_error:.6f}")

    if abs_error < tol:
        print("\nConverged successfully!")
        root = x_new
        break

    x = x_new

else:
    print("\nMethod did not converge within the maximum iterations.")
    root = x

# Function plot
x_vals = np.linspace(root-2, root+2, num=400)
y_vals = f(x_vals)

plt.figure(figsize=(12,5))

# Function plot
plt.subplot(1,2,1)
plt.axhline(0, color='black')
plt.plot(x_vals, y_vals, label='f(x)')
plt.plot(root, f(root), marker='o', color='red', label='Root')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function Plot")
plt.legend()

# Error plot
plt.subplot(1,2,2)
plt.plot(iterations, errors, marker='o')
plt.xlabel("Iteration number")
plt.ylabel("Absolute error")
plt.title("Error vs Iteration")

plt.tight_layout()
plt.show()
