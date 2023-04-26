#Ejercicio sin restar inventario
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

def precioFinal(obj):
    return obj.getPrecioBase()

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
    while item != 'fin':
        for i in range(3):
            for j in data[i]:
                if j.getIdArticulo() == int(item):
                    carrito[i].append(j)
        item=input('Id del item: ')
    #print(carrito)
    return carrito

def imprimir(carrito):
    titulos=['Bebidas','Condimentos','Lacteos']
    venta=0
    total=0
    for i in range(3):
        for j in carrito[i]:
            venta += precioFinal(j) 
        total +=venta  
        print(f'Total {titulos[i]}: {venta}')
        venta=0
    print(f'Valor Total: {total}')

def main():
    data=lectura()
    carrito = facturar(data)
    imprimir(carrito)

if __name__=="__main__":
    main()