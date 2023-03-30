
Archivo = open('Alimentos.txt','rt')
informacion = Archivo.readlines()
datos=[]
for i in informacion:
    datos.append(i.rstrip('\n').split(','))
print(datos)

tabla = Archivo.read().split('\n')
datos=[]
for i in range(len(tabla)):
    datos.append(tabla[i].split(','))
print(datos)
