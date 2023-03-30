class Deportista:
    def __init__(self,nombre,documento,edad):
        self.__nombre=nombre
        self.__documento=documento
        self.__edad=edad

    # def __init__(self):
    #     self.__nombre=None
    #     self.__documento=None
    #     self.__edad=None
    
    #----------------Getters-----------------
    def getNombre(self):
        return self.__nombre
    
    def getDocumento(self):
        return self.__documento

    def getEdad(self):
        return self.__edad

    #----------------Setters-----------------
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setDocumento(self,documento:int):
        self.__documento=documento

    def setEdad(self,edad:int):
        self.__edad=edad

    #------------ Sobrecarga del método --------------
    def Medalla():
        print('Recibe una medalla')

class DeportistaFutbol(Deportista):
    def __init__(self,nombre:str,documento:int,edad:int,goles:int,nombreEquipo:str):
        super().__init__(nombre,documento,edad)
        self.__goles=goles
        self.__equipo=nombreEquipo

    # def __init__(self,goles:int,nombreEquipo:str):
    #     super().__init__()
    #     self.__goles=goles
    #     self.__equipo=nombreEquipo

    #----------------Getters-----------------    
    def getEquipo(self):
        return self.__equipo
        
    def getGoles(self):
        return self.__goles
    
    #----------------Setters-----------------
    def setEquipo(self,nombreEquipo:str):
        self.__equipo=nombreEquipo

    def setGoles(self,goles:int):
        self.__goles=goles

    #------------ método heredado --------------
    def anotar(self, goles:int):
        self.__goles +=goles
    
    #------------ Sobrecarga de método ---------
    def Medalla():
        print('Recibe otra medalla')
        
def main():
    deportista = DeportistaFutbol('Falcao',122546,34,24,'Rayo Vallecano')
    segundo = Deportista('Yepes', 54513224, 45)
    DeportistaFutbol.Medalla()
    Deportista.Medalla()

    # deportista = DeportistaFutbol(24,'Rayo Vallecano')
    # deportista.setNombre('Falcao')
    # deportista.setDocumento(122546)
    # deportista.setEdad(34)

    print(f'Deportista: {deportista.getNombre()} -CC: {deportista.getDocumento()} -Edad: {deportista.getEdad()}')
    print(f'Equipo: {deportista.getEquipo()} -#Goles: {deportista.getGoles()}')
    deportista.anotar(3)
    print(f'#Goles: {deportista.getGoles()}')
    print(deportista.__sizeof__())  #Establece el tamaño del objeto en la memoria 

if __name__ == "__main__":
    main()