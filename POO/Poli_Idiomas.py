class Ciudadano():
    def __init__(self,idioma,nombre):
        self.__idioma=idioma
        self.__nombre=nombre

    def setIdioma(self,idioma):
        self.__idioma = idioma

    def setNombre(self,nombre):
        self.__nombre =nombre
    
    def getIdioma(self):
        return self.__idioma
    
    def getNombre(self):
        return self.__nombre
    
    # -------------- PoliMorfismo ----------------
    def Saludo(self):
        print('Quoi de beau!')
    
class Colombia(Ciudadano):
    def __init__(self,idioma,nombre):
        super().__init__(idioma,nombre)
        self.CC=None
    
    def setCC(self,CC):
        self.CC = CC
    
    def getCC(self):
        return self.CC
    
    # -------------- PoliMorfismo ----------------
    def Saludo(self):
        print('Qiubo pues home!')

class Inglaterra(Ciudadano):
    def __init__(self,idioma,nombre):
        super().__init__(idioma,nombre)
        self.Id=None
    
    def setId(self,Id):
        self.Id = Id
    
    def getId(self):
        return self.Id

    # -------------- PoliMorfismo ----------------
    def Saludo(self):
        print('Hello bro!')

class China(Ciudadano):
    def __init__(self,idioma,nombre):
        super().__init__(idioma,nombre)
        self.Shengfenzheng=None

    def setShengfenzheng(self,Shengfenzheng):
        self.Shengfenzheng = Shengfenzheng
    
    def getShengfenzheng(self):
        return self.Shengfenzheng
    
    # -------------- PoliMorfismo ----------------
    def Saludo(self):
        print('你干嘛呀!')

def darSaludo(objeto):
    objeto.Saludo()
    

def main():
    
    Ciudadano1 = Colombia('español','David')
    Ciudadano2 = Inglaterra('ingles','Mike')
    Ciudadano3 = China('Mandarin','Liu')
    Ciudadano4 = Ciudadano('Frances','Carla')

    print(f'Aplicante: {Ciudadano1.getNombre()}, Idioma: {Ciudadano1.getIdioma()}')
    print(f'Aplicante: {Ciudadano2.getNombre()}, Idioma: {Ciudadano2.getIdioma()}')
    print(f'Aplicante: {Ciudadano3.getNombre()}, Idioma: {Ciudadano3.getIdioma()}')
    darSaludo(Ciudadano1)
    darSaludo(Ciudadano2)
    darSaludo(Ciudadano3)
    darSaludo(Ciudadano4)
    

if __name__ == "__main__":
    main()