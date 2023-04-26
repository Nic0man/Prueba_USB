class Articulos():
    def __init__(self):
        self.__Idarticulo=None
        self.__precioBase=None
        self.__unidExistencia=None
    
    def setIdArticulo(self,Id:int):
        self.__Idarticulo=Id
    
    def setPrecioBase(self,precio:float):
        self.__precioBase=precio
    
    def setUnidExistencia(self,unidad:int):
        self.__unidExistencia=unidad

    def getIdArticulo(self):
        return self.__Idarticulo
    
    def getPrecioBase(self):
        return self.__precioBase
    
    def getUnidExistencia(self):
        return self.__unidExistencia

class Bebidas(Articulos):
    def __init__(self):
        super().__init__()
        self.__cantUnidad=None
        self.__proveedor=None
    
    def setCantUnidad(self, cantidad:str):
        self.__cantUnidad=cantidad
    
    def setProveedor(self, proveedor:str):
        self.__proveedor=proveedor

    def getCantUnidad(self):
        return self.__cantUnidad
    
    def getProveedor(self):
        return self.__proveedor

    def precioFinal(self):
        precio = self.getPrecioBase() * 1.19
        return round(precio,2)  
  
class Lacteos(Articulos):
    def __init__(self):
        super().__init__()
        self.__cantUnidad=None
        self.__proveedor=None
    
    def setCantUnidad(self, cantidad:str):
        self.__cantUnidad=cantidad
    
    def setProveedor(self, proveedor:str):
        self.__proveedor=proveedor

    def getCantUnidad(self):
        return self.__cantUnidad
    
    def getProveedor(self):
        return self.__proveedor

    def precioFinal(self):
        return self.getPrecioBase()

class Condimentos(Articulos):
    def __init__(self):
        super().__init__()
        self.__cantUnidad=None
        self.__proveedor=None
    
    def setCantUnidad(self, cantidad:str):
        self.__cantUnidad=cantidad
    
    def setProveedor(self, proveedor:str):
        self.__proveedor=proveedor

    def getCantUnidad(self):
        return self.__cantUnidad
    
    def getProveedor(self):
        return self.__proveedor

    def precioFinal(self):
        precio = self.getPrecioBase() * 1.05
        return round(precio,2)    

def precioFinal(obj):
    return obj.precioFinal()

def lectura():
    n = open('Catalogo.csv','rt')
    data = [[],[],[]]
    linea = n.readline().rstrip('\n').split(',')
    while linea != ['']:
        if linea[3]=='Bebidas':
            obj = Bebidas()
            obj.setIdArticulo(int(linea[0]))
            obj.setPrecioBase(float(linea[5].rstrip('USD')))
            obj.setUnidExistencia(int(linea[6]))
            obj.setCantUnidad(linea[4])
            obj.setProveedor(linea[2])
            data[0].append(obj)
        elif linea[3]=='Condimentos':
            obj = Condimentos()
            obj.setIdArticulo(int(linea[0]))
            obj.setPrecioBase(float(linea[5].rstrip('USD')))
            obj.setUnidExistencia(int(linea[6]))
            obj.setCantUnidad(linea[4])
            obj.setProveedor(linea[2])
            data[1].append(obj)
        elif linea[3]=='LÃ¡cteos':
            obj = Lacteos()
            obj.setIdArticulo(int(linea[0]))
            obj.setPrecioBase(float(linea[5].rstrip('USD')))
            obj.setUnidExistencia(int(linea[6]))
            obj.setCantUnidad(linea[4])
            obj.setProveedor(linea[2])
            data[2].append(obj)
        linea = n.readline().rstrip('\n').split(',')

    n.close()
    # print(f'Bebidas:')
    #print(data[0][1].getIdArticulo())
    # print(f'Condimentos:')
    # print(data[1])
    # print(f'Lácteos:')
    # print(data[2])
    return data

def facturar(data): 

    carrito=[[],[],[]]
    item=input('Id del item: ')
    while item.lower() != 'fin':
        for i in range(3):
            for j in data[i]:
                if (j.getIdArticulo() == int(item)) and (j.getUnidExistencia() > 0):
                    carrito[i].append(j)
                    j.setUnidExistencia(j.getUnidExistencia() - 1)
                elif (j.getIdArticulo() == int(item)) and (j.getUnidExistencia() == 0):
                    print('Existencia Insuficiente')
        if int(item)>34 or item=='':
            print('Ingreso de Código erroneo')        
        item=input('Id del item: ')
    print('\n')
    #print(carrito)
    return carrito

def imprimir(carrito):
    titulos=['Bebidas    ','Condimentos','Lacteos    ']
    venta=0
    total=0

    print('--------------------------------------\n'+'---------- Factura de Venta ----------\n'\
        +'---------Supermercado LA GRANJA-------\n'\
            +''+'Categoria     Cantidad     Precio Acu\n')

    for i in range(3):
        for j in carrito[i]:
            venta += precioFinal(j) 
        total +=venta  
        print(f'{titulos[i]}..... {len(carrito[i])} ........ {venta} USD')
        venta=0
    print(f'--------------------------------------\n'+F'Valor Total: .............. {total} USD\n')

def main():
    data=lectura()
    carrito = facturar(data)
    imprimir(carrito)

if __name__=="__main__":
    main()