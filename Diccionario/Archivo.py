

def main():
    dicc = {}
    f=open('matrizAsignacion.txt','rt')
    matriz = f.readlines()
    f.seek(0)
    matriz1 = f.read()
    print(matriz1)
    
    suma=0
    for i in range(len(matriz)):
        valor=f.readline().rstrip('\n').split(',')
        for j in range(len(valor)):
            pos = str(f'{i}{j}')
            dicc[pos] = valor[j]

    print(dicc) 
    f.close()

    busqueda.busqueda_dicc(dicc)
     
    

if __name__=="__main__":
    main()