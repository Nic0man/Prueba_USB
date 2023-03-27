def suma(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return(lista[0] + suma(lista[1:])) #[1:] toma todos los elementos de la lista, excepto el primero.
    

lista = [1,2,3,4,5]
print(suma(lista))
