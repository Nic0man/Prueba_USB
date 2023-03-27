class Persona():

    def __init__(self):
        self.__nombre=None
        self.__edad=None
        self.__dni=None
    
    # ------------ Getters --------------
    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getDni(self):
        return self.__dni
    
    # ------------- Setters ---------------
    def setNombre(self,nombre):
        self.__nombre=nombre
      
    def setDni(self,dni):
        self.__dni=dni
        self.validar_dni()
    
    def setEdad(self,edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad=0
        else:
            self.__edad=edad

    # --------------- Métodos -------------
    def validar_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"

        if len(self.__dni)!=9:
            print("DNI incorrecto!")
            self.__dni = ""
        else:
            letra = self.__dni[8]
            num = int(self.__dni[:8])
            print(letras[num % 23])
            if letra.upper() != letras[num % 23]:
                print("DNI incorrecto")
                self.__dni = ""
    
    def mostrar(self):
        return "Nombre:"+self.__nombre+" - Edad:"+str(self.__edad)+" - DNI:"+self.__dni

    def esMayorDeEdad(self):
        if self.__edad>=18:
          print('Es mayor de edad')
        else:
          print('No es mayor de edad')
        
  
def main():
  Cliente = Persona()
  Cliente.setNombre('Nicolas')
  Cliente.setDni('23456783A')
  Cliente.setEdad(30)

  print(f'{Cliente.mostrar()}')
  Cliente.esMayorDeEdad()

if __name__=="__main__":
  main()