# Uses python3

def change(a):
    coins = 0
    while a > 0:
        if (a - 10) >= 0:
            a = a -10
            coins += 1
        elif (a - 5) >= 0:
            a = a -5
            coins += 1
        elif (a - 1) >= 0:
            a = a - 1
            coins += 1
    return coins

n = int(input())
print(change(n))
