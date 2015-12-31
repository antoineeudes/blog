from math import exp

a = input("a?")

def u(n, a):
    u = a
    for k in range(n+1):
        u = exp(u) / (n+2)

n = input("n?")
print(n, a)
