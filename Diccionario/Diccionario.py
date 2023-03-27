n = int(input('Ingrese un numero: '))
dicc = {}

doc = open('matrizAsignacion.txt','rt')

for i in range(n):
    informacion = doc.readline()
    lista = informacion.rstrip('\n').split(',')
    print(lista)
    pos = ''
    for j in range(len(lista)):
        pos = str(f'{i}{j}')
        dicc[pos] = lista[j]

print(dicc)
print(f'el dato seleccionado es {dicc["20"]}')

