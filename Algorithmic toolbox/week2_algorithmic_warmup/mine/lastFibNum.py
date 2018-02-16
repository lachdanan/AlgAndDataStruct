# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append((fib[i-1] + fib[i-2]) % 10)
    return fib[n]

n = int(input())
print(calc_fib(n))
