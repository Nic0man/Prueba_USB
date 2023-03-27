#funcion recursiva para calcular K(n,p) = 0p + 1p + 2p + 3p + .... np 

def sumatoria(n,p):
    if n > 0:
        print(n,p)
        x = ((n * p) + (sumatoria(n-1,p))) 
        return x
    else:
        return 0


n = int(input('ingrese el valor de n '))
p = int(input('ingrese el valor de p '))
print(sumatoria(n,p))
