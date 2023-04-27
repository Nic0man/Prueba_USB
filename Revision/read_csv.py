#Jose David Gil
#Juan Felipe Reina

import csv

def lectura():
    n = open('Catalogo.csv','rt')
    data = []
    linea = n.readline()
    while linea != '':
        data.append(linea.rstrip('\n').split(','))
        linea = n.readline()
    n.close()
    return data

id_productos = {}

with open('Catalogo.csv') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)  # saltar la primera fila (encabezados)
    for fila in lector_csv:
        IdProducto = fila[0]
        if IdProducto not in id_productos:
            id_productos[IdProducto] = []
        id_productos[IdProducto].append(fila)

print('Muestra el id de los productos')
for i, IdProducto in enumerate(id_productos.keys()):
    print(f'{i+1}. {IdProducto}')

nombre_producto = {}

with open('Catalogo.csv') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)  # saltar la primera fila (encabezados)
    for fila in lector_csv:
        nombre = fila[1]
        if nombre not in nombre_producto:
            nombre_producto[nombre] = []
        nombre_producto[nombre].append(fila)

print('Muestra el nombre de los productos')
for i, nombre_producto in enumerate(nombre_producto.keys()):
    print(f'{i+1}. {nombre_producto}')


proveedor_producto = {}

with open('Catalogo.csv') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)  # saltar la primera fila (encabezados)
    for fila in lector_csv:
        proveedor = fila[2]
        if proveedor not in proveedor_producto:
            proveedor_producto[proveedor] = []
        proveedor_producto[proveedor].append(fila)

print('Muestra proveedor de los produtos')
for i, proveedor_producto in enumerate(proveedor_producto.keys()):
    print(f'{i+19}. {proveedor_producto}')


categoria_producto = {}

with open('Catalogo.csv') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)  # saltar la primera fila (encabezados)
    for fila in lector_csv:
        categoria = fila[3]
        if categoria not in categoria_producto:
            categoria_producto[categoria] = []
        categoria_producto[categoria].append(fila)

print('Muestra categoria de los produtos')
for i, categoria_producto in enumerate(categoria_producto.keys()):
    print(f'{i+1}. {categoria_producto}')
