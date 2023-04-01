
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

def companias(data):
    pais=[]
    for i in data[1:]:
        country=i[4]
        if country not in pais:
            pais.append(country)
    pais.sort()
    print(pais.__len__())
    return(pais)

def busqueda(data,pais):
    search=int(input('Indice del país de busqueda: '))
    
    empresas=[]
    empleados=[]
    for i in data:
        if i[4]==pais[search-1]:
            empresas.append(i)
            empleados.append(int(i[8]))
    #print(empresas.__len__())
    return empresas,empleados

def analisisDatos(empresas,empleados):
    print(f'\nPais:{empresas[0][4]}\n')

    print('Empresa con mayor # de empleados:')
    mayor=empleados.index(max(empleados))
    print(f'- Empresa:{empresas[mayor][2]}\n- Website:{empresas[mayor][3]}')
    print(f'- Descripción:{empresas[mayor][5]}\n- Fundación:{empresas[mayor][6]}')
    print(f'- Industria:{empresas[mayor][7]}\n- #Empleados:{empresas[mayor][8]}\n')

    print('Empresa con menor # de empleados:')
    menor=empleados.index(min(empleados))
    print(f'- Empresa:{empresas[menor][2]}\n- Website:{empresas[menor][3]}')
    print(f'- Descripción:{empresas[menor][5]}\n- Fundación:{empresas[menor][6]}')
    print(f'- Industria:{empresas[menor][7]}\n- #Empleados:{empresas[menor][8]}\n')

    promedio=round(sum(empleados)/len(empleados),2)
    print(f'Promedio empleos: {promedio}')

def main():
    data=lectura()
    data_pais=companias(data)
    data_busqueda,data_empleados=busqueda(data,data_pais)
    analisisDatos(data_busqueda,data_empleados)



if __name__=="__main__":
    main()