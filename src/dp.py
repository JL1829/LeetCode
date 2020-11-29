def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(10))


def fibonacci_dp(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(fibonacci_dp(10))


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 1000000007
    return a


print(fibonacci(10))
