# Uses python3
import sys

def euclidgcd(a, b):
    remainder = 1
    values = [a,b]
    while remainder > 0:
        remainder = values[0] % values[1]
        values[0] = values[1]
        values[1] = remainder
    return values[0]

def lcd(a, b):
    if b == 0:
        return a
    return (a * b) // euclidgcd(a, b)

data = input()
tokens = data.split()
a = int(tokens[0])
b = int(tokens[1])
print(lcd(a, b))
