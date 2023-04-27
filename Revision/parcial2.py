class Articulos():
    def __init__(self):
        self.__idArticulo=None
        self.__precioBase=None
        self.__unidExistencia=None
    #Setters
    def setPrecioBase(self,precioBase : float):
        self.__precioBase=precioBase
    def setunidExistencia(self,unidExistencia : int):
        self.__unidExistencia=unidExistencia
    #Getters
    def getPrecioBase(self):
        return self.__precioBase
    def getunitExistencia(self):
        return self.__unidExistencia
    
    def precioFinal(self):
        pass
    def Facturar(self,id):
        pass
        
class Bebidas(Articulos):
    def __init__(self):
        super().__init__()
        self.__cantUnidad=None
        self.__proveedor=None
    #Setters
    def setcantUnidad (self, cantUnidad : str):
        self.__cantUnidad=cantUnidad
    def setProveedor (self, proveedor : str):
        self.__proveedor=proveedor
    #Getters
    def getcantUnidad(self):
        return self.__cantUnidad
    def getProveedor(self):
        return self.__proveedor

    def PrecioFinal(self):
        pass
class Lacteos(Articulos):
    def __init__(self):
        super().__init__()
        self.__cantUnidad=None
        self.__proveedor=None
    #Setters
    def setcantUnidad (self, cantUnidad : str):
        self.__cantUnidad=cantUnidad
    def setProveedor (self, proveedor : str):
        self.__proveedor=proveedor
    #Getters
    def getcantUnidad(self):
        return self.__cantUnidad
    def getProveedor(self):
        return self.__proveedor

    def PrecioFinal(self):
        pass
class Condimentos(Articulos):
    def __init__(self):
        super().__init__()
        self.__cantUnidad=None
        self.__proveedor=None
    #Setters
    def setcantUnidad (self, cantUnidad : str):
        self.__cantUnidad=cantUnidad
    def setProveedor (self, proveedor : str):
        self.__proveedor=proveedor
    #Getters
    def getcantUnidad(self):
        return self.__cantUnidad
    def getProveedor(self):
        return self.__proveedor

    def PrecioFinal(self):
        pass



