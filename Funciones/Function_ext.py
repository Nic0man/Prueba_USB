
def main(nombre):
    print(f'Hola {nombre}')
    print(f'impreso desde => {__name__}')

if __name__ == "__main__":
    nombre = ''
    main(nombre)
else:
    print('no se ejecutó desde Function_ext.py')

    