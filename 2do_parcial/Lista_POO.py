class Ciudadano():
    def __init__(self):
        self.__idioma=None
        self.__nombre=None

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
        print("What's up bro!")

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
    
    ciudadanos = []
    for i in range(4):
        persona =Ciudadano()
        persona.setIdioma(input('Ingrese el idioma '))
        persona.setNombre(input('Ingrese el nombre '))
        print('objeto creado exitosamente')
        ciudadanos.append(persona)

    print('---------- Ciudadanos del mundo ----------')
    for i in range(4):
        print(f'Aplicante: {ciudadanos[i].getNombre()}, Idioma: {ciudadanos[i].getIdioma()}')
        print('-------- Como saludan en el mundo --------')
        darSaludo(ciudadanos[i])

    


if __name__ == "__main__":
    main()