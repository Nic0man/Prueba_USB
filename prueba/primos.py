def primos(x):
    num = 1
    j = 1
    status = 0
    con = 0
    impresion = ''
    while con <= x:
        while j <= num:
            primo = num % j
            if primo == 0:
                if num == j and status == 0:
                    impresion += str(f'{num},')
                    con +=1
                    break
                status = 1
            j += 1
        num += 1
        j=2
        status = 0
    print(impresion)

def main():
    x = int(input('Indique la cantidad de numeros primos: '))
    primos(x)


if __name__ == "__main__":
    main()