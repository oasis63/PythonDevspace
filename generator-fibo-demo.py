def fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()

fib_10 = [next(fib) for _ in range(10)]

print(fib_10)

print("11ths fib number ")
print(next(fib))
