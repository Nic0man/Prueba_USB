

class Persona:
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.edad = None
        self.frase = None
    
    def Hablar(self):
        return self.frase

def main():
    Profesor = Persona()
    Profesor.nombre = 'Javier'
    Profesor.apellido = 'Gomez'
    Profesor.edad = 21
    Profesor.frase = 'Vamos a programar en Python'

    Piloto = Persona()
    Piloto.nombre = 'Fernando'
    Piloto.apellido = 'Perez'
    Piloto.edad = 32
    Piloto.frase = 'Bienvenidos al vuelo 985'

    print(f'Atención estudiantes: {Profesor.Hablar()}')
    print(f'Atención Pasajeros: {Piloto.Hablar()}')

if __name__ == "__main__":
    main()


