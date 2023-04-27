# Mauricoi Mora Rueda   y   Satiago Blanco Peñuela

import csv

class Articulo():
    def __init__(self, idArticulo, precioBase, unidExistencia):
        self.__idArticulo = idArticulo
        self.__precioBase = precioBase
        self.__unidExistencia = unidExistencia

    def getIdArticulo(self):
        return self.__idArticulo

    def getPrecioBase(self):
        return self.__precioBase

    def getUnidExistencia(self):
        return self.__unidExistencia

    # setters
    def setIdArticulo(self, idArticulo):
        self.__idArticulo = idArticulo

    def setPrecioBase(self, precioBase):
        self.__precioBase = precioBase

    def setUnidExistencia(self, unidExistencia):
        self.__unidExistencia = unidExistencia


class Bebidas(Articulo):
    def __init__(self, idArticulo, nombre, precioBase, unidExistencia, cantUnidad, proveedor):
        super().__init__(idArticulo, precioBase, unidExistencia)
        self.__nombre = nombre
        self.__cantUnidad = cantUnidad
        self.__proveedor = proveedor

    def getNombre(self):
        return self.__nombre

    def getCantUnidad(self):
        return self.__cantUnidad

    def getProveedor(self):
        return self.__proveedor

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setCantUnidad(self, cantUnidad):
        self.__cantUnidad = cantUnidad

    def setProveedor(self, proveedor):
        self.__proveedor = proveedor


class Lacteos(Articulo):
    def __init__(self, idArticulo, nombre, precioBase, unidExistencia, cantUnidad, proveedor):
        super().__init__(idArticulo, precioBase, unidExistencia)
        self.__nombre = nombre
        self.__cantUnidad = cantUnidad
        self.__proveedor = proveedor

    def getNombre(self):
        return self.__nombre

    def getCantUnidad(self):
        return self.__cantUnidad

    def getProveedor(self):
        return self.__proveedor

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setCantUnidad(self, cantUnidad):
        self.__cantUnidad = cantUnidad

    def setProveedor(self, proveedor):
        self.__proveedor = proveedor


class Condimentos(Articulo):
    def __init__(self, idArticulo, nombre, precioBase, unidExistencia, cantUnidad, proveedor):
        super().__init__(idArticulo, precioBase, unidExistencia)
        self.__nombre = nombre
        self.__cantUnidad = cantUnidad
        self.__proveedor = proveedor

    def getNombre(self):
        return self.__nombre

    def getCantUnidad(self):
        return self.__cantUnidad

    def getPrecio(self):
        return self.__precio

    def getExistencia(self):
        return self.__existencia

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setCantUnidad(self, cantUnidad):
        self.__cantUnidad = cantUnidad

    def setPrecio(self, precio):
        self.__precio = precio

    def setExistencia(self, existencia):
        self.__existencia = existencia

def leer_catalogo():
    with open('catalogo.csv', newline='') as archivo:
        lector = csv.reader(archivo)
        next(lector)
        bebidas = []
        lacteos = []
        condimentos = []
        for fila in lector:
            id = fila[0]
            nombre = fila[1]
            precio = fila[2]
            existencia = fila[3]
            categoria = fila[4]
            if categoria == 'Bebidas':
                bebidas.append(Bebidas(id, nombre, precio, existencia))
            elif categoria == 'Lacteos':
                lacteos.append(Lacteos(id, nombre, precio, existencia))
            elif categoria == 'Condimentos':
                condimentos.append(Condimentos(id, nombre, precio, existencia))
    return bebidas, lacteos, condimentos

def facturar():
    bebidas, lacteos, condimentos = leer_catalogo()
    total_bebidas = 0
    total_lacteos = 0
    total_condimentos = 0
    while True:
        print("Ingrese el ID del artículo que desea comprar o '0' para salir: ")
        id = input()
        if id == '0':
            break
        print("Ingrese la cantidad que desea comprar: ")
        cant = int(input())
        encontrado = False
        for bebida in bebidas:
            if bebida.getId() == id:
                encontrado = True
                if bebida.verificarExistencia(cant):
                    bebida.descontarExistencia(cant)
                    total_bebidas += cant * bebida.getPrecio()
                    print(f"Artículo: {bebida.getNombre()}, cantidad: {cant}, precio unitario: {bebida.getPrecio()}")
                else:
                    print("No hay suficientes existencias de este artículo")
        for lacteo in lacteos:
            if lacteo.getId() == id:
                encontrado = True
                if lacteo.verificarExistencia(cant):
                    lacteo.descontarExistencia(cant)
                    total_lacteos += cant * lacteo.getPrecio()
                    print(f"Artículo: {lacteo.getNombre()}, cantidad: {cant}, precio unitario: {lacteo.getPrecio()}")
                else:
                    print("No hay suficientes existencias de este artículo")
        for condimento in condimentos:
            if condimento.getId() == id:
                encontrado = True
                if condimento.verificarExistencia(cant):
                    condimento.descontarExistencia(cant)
                    total_condimentos += cant * condimento.getPrecio()
                    print(f"Artículo: {condimento.getNombre()}, cantidad: {cant}, precio unitario: {condimento.getPrecio()}")
                else:
                    print("No hay suficientes existencias de este artículo")
        if not encontrado:
            print("ID de artículo no encontrado")
    print(f"Total de bebidas: {total_bebidas}")
    print(f"Total de lácteos: {total_lacteos}")
    print(f"Total de condimentos: {total_condimentos}")

def main():
    bebidas, lacteos, condimentos = leer_catalogo()


    print("Categorias disponibles:")
    print("- Bebidas")
    print("- Lacteos")
    print("- Condimentos")


    categoria = input("Ingrese la categoria del articulo a facturar: ")


    while categoria not in ["Bebidas", "Lacteos", "Condimentos"]:
        print("Categoria no valida. Por favor ingrese una categoria valida.")
        categoria = input("Ingrese la categoria del articulo a facturar: ")


    codigo = input("Ingrese el codigo del articulo a facturar: ")

    articulo = verificar_existencia(bebidas, lacteos, condimentos, categoria, codigo)

    if articulo is not None:
        cantidad = int(input("Ingrese la cantidad de unidades a facturar: "))
        total = facturar(articulo, cantidad)
        print(f"Total a pagar: ${total}")
    else:
        print("El articulo no se encuentra en el inventario.")

if __name__ == '__main__':
    main()

