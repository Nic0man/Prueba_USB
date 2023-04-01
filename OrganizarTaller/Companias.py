def escritura(data):
    pais=[]
    for i in data[1:]:
        country=i[4]
        if country not in pais:
            pais.append(country)
    pais.sort()
    return(pais)

    # f=open('organizations-100.csv','w')
    # for i in pais:
    #     f.write(str(f'{i}\n'))
    # f.close()

def lectura():
    f=open('organizations-10000.csv','r')
    data = []
    final=0;con=0
    while final!=1:
        linea = f.readline()
        if linea == '':
            final=1
        else:
            data.append(linea.rstrip('\n').split(','))
            con +=1
    #print(data[4])
    f.close()
    print('contador ',con)
    return data

def indice(data,pais):
    pos=[]
    for i in data:
        for j in pais:
            if i[4]==j:
                pos.append(pais.index(j)+1)
    print(pos[:20])

    # f=open('organizations-100.csv','w')
    # for i in pos:
    #     f.write(str(f'{i}\n'))
    # f.close()

def main():
    data=lectura()          #Lee todas las lineas del archivo csv
    data_pais=escritura(data)       #Crea una matriz con los paises del archivo
    indice(data,data_pais)          #crea una matriz con los indices de cada país
    


if __name__=="__main__":
    main()