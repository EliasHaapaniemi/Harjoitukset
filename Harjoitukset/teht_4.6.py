import random

N = int(input("Anna pisteiden määrä: "))

n = 0
i = 0

while i < N:
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1

    if x*x + y*y < 1:
        n = n + 1

    i = i + 1

pi = 4 * n / N

print(pi)