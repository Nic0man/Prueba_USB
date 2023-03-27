class Personas:
  def __init__(self):
    self.__nombre=None
    self.__altura=None
    self.__peso=None
  
  def setNombre(self,nombre:str):
    self.__nombre= nombre

  def getNombre(self):
    return self.__nombre
  
  def setAltura(self,altura:int):
    self.__altura=altura
  
  def getAltura(self):
    return self.__altura

  def setPeso(self,peso:int):
    self.__peso=peso
  
  def getPeso(self):
    return self.__peso

  def __IMC(self):
    imc = self.__peso / ((self.__altura/100)**2)
    return imc

  def getIMC(self):
    return self.__IMC()


def main():
  Cliente = Personas()
  Cliente.setNombre('Julian')
  Cliente.setAltura(170)
  Cliente.setPeso(70)
  print(f'El cliente {Cliente.getNombre()} tiene IMC de {Cliente.getIMC()}')

if __name__ == "__main__":
  main()