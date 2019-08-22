fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)


def fib(n):
    if n <= 2:
        return n
    return fib(n - 1) + fib(n - 2)
fib = fib(9)
print(fib)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


fib = fib(6)
print(fib)
