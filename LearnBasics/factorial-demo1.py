def factorial(n):
    if n == 0 or n == 1:
        return n
    return n * factorial(n - 1)


memo = [-1] * 100


def fibo(n):
    if n == 0 or n == 1:
        return n

    if memo[n] != -1:
        return memo[n]

    memo[n] = fibo(n - 1) + fibo(n - 2)

    return memo[n]


def main():
    for n in range(10):
        # print(n, " ---> ", factorial(n))
        print(n, " ---> ", fibo(n))


main()
