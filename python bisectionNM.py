def bisection(f, a, b, tol=1e-6, max_iter=50):
    if f(a) * f(b) >= 0:
        print("Bisection method fails: f(a) and f(b) must have opposite signs.")
        return None

    print("Iter |    a       b       c      f(c)      |b-a|     Stop reason")
    print("----------------------------------------------------------------")

    c_old = None

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        interval = abs(b - a)
        stop_reason = ""

        if c_old is not None:
            root_error = abs(c - c_old)
        else:
            root_error = None

        # stopping conditions
        if abs(fc) < tol:
            stop_reason = "f(c) small"
        elif interval / 2 < tol:
            stop_reason = "interval small"
        elif root_error is not None and root_error < tol:
            stop_reason = "root error small"
        elif i == max_iter:
            stop_reason = "max iter reached"

        print(f"{i:4d} | {a:8.5f} {b:8.5f} {c:8.5f} {fc:10.6f} {interval:10.6f} {stop_reason}")

        if stop_reason:
            return c

        # update interval
        if f(a) * fc < 0:
            b = c
        else:
            a = c

        c_old = c

    return c


f = lambda x: x**3 - x - 2
root = bisection(f, a=1, b=2, tol=1e-6, max_iter=30)
print("\nApproximate root:", root)
