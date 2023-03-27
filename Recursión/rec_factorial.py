import sys
sys.setrecursionlimit(5000) # Modificación del límite de recursiones

def factorial(x):
    if x==0:
        return 1
    else:
        fac = x*factorial(x-1)
        return fac

x = int(input('ingrese un numero '))
fac = factorial(x)
print("El factorial de", x, "es", fac)