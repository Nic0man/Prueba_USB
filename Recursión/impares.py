def impar(n):
    if n <= 0:
        return 0
    else:
        return((2*n-1) + impar(n-1))
        

n = int(input('Ingrese el numero de numeros impares que desea generar: '))
for i in range(n):
    x=impar(i)
    print(x)