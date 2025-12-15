# Newton-Raphson Method

# function
def f(x):
    return x**3 - x - 1

# derivative
def df(x):
    return 3*x**2 - 1

x0 = float(input("Enter initial guess x0: "))
tol = float(input("Enter absolute error tolerance: "))
max_iter = int(input("Enter maximum number of iterations: "))

x = x0

print("\nIter\t x_n\t\t f(x_n)\t\t Absolute Error")

for i in range(1, max_iter + 1):

    if df(x) == 0:
        print("Derivative is zero. Method fails.")
        break

    x_new = x - f(x) / df(x)
    abs_error = abs(x_new - x)

    print(f"{i}\t {x_new:.6f}\t {f(x_new):.6f}\t {abs_error:.6f}")

    if abs_error < tol:
        print("\nConverged successfully!")
        print("Root =", round(x_new, 6))
        break

    x = x_new

else:
    print("\nMethod did not converge within the maximum iterations.")
