# Uses python3
import sys

def euclidgcd(a, b):
    if b == 0:
        return a
    remainder = 1
    values = [a,b]
    while remainder > 0:
        remainder = values[0] % values[1]
        values[0] = values[1]
        values[1] = remainder
    return values[0]
    
data = input()
tokens = data.split()
a = int(tokens[0])
b = int(tokens[1])
print(euclidgcd(a, b))
