# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
max1 = 0
max2 = 0
if n == 2:
    max1 = a[0]
    max2 = a[1]
else:
    for i in range(0, n):
        if a[i] > max1:
            max2 = max1
            max1 = a[i]
        elif a[i] > max2:
            max2 = a[i]

result = max1 * max2
print(result)
