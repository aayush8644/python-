def fib_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# Get nth Fibonacci number
print(fib_recursive(10))  # Output: 34
