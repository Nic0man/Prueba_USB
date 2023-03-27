def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)
        return fib  



n = int(input('Cuantos numeros desea generar: '))
for i in range(n):
    fib = fibonacci(i)
    print(fib, end=', ')
