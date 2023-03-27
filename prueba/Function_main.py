import Function_ext

def main():
    nombre = input('ingrese un nombre => ')
    Function_ext.main(nombre)
    print('impreso desde =>',__name__)

if __name__== "__main__":
    main()

    