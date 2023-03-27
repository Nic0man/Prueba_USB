
# def ejemplo1():
#     miArchivo = open('miarchivo.txt', 'r')
#     informacion = miArchivo.read(10)
#     print(informacion)
#     print(len(informacion))
#     miArchivo.close()



# def ejemplo2():
#     miArchivo = open('miarchivo.txt', 'r')
#     linea = miArchivo.readlines()
#     print(linea, end=', ')
#     print("Lei la primera línea. Vamos a la segunda.")
#     linea = miArchivo.readlines()
#     print(linea)
#     miArchivo.close()


def ejemplo3():
    miArchivo = open('miarchivo.txt', 'w')
    lista = ['era', 'una', 'lagartija']
    miArchivo.writelines(lista)
    miArchivo.close()

# import os

# def cls():
#     os.system('cls' if os.name == 'nt' else 'clear')


# def matriz():
#     x = []
#     miArchivo = open('matrizAsignacion.txt', 'r')
#     informacion = miArchivo.readline()
#     while informacion:
#         fila = informacion.rstrip('\n').split(',')
#         x.append(fila)
#         informacion = miArchivo.readline()
#     """
#     información = miArchivo.read()
#     datos = informacion.split('\n')
#     for rows in datos:
#         x.append(rows.split(','))
#     """
#     miArchivo.close()
#     print(x)
#     print(x[2][2])


def App():
    #ejemplo1()
#-------------------
    #ejemplo2()
#-------------------
    ejemplo3()
#-------------------
    #cls()
    # matriz()




if __name__ == '__main__':
    App()