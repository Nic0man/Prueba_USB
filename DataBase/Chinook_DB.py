import sqlite3

def validar(usuario):
    db=sqlite3.connect("datos.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    #consulta="select * from Usuarios where apellido='" + usuario +"'"
    consulta="select * from Usuarios"
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    for i in resultado:
        print(list(i))
    # for i in resultado:
    #     for j in i:
    #         print(j,end=' ')
    #     print('\n')
    cursor.close()
    db.close()
    return resultado

def main():
    nombre=input('Ingrese el nombre: ')
    apellido=input('Ingrese el apellido: ')
    edad=int(input('Ingrese la edad: '))
    validar('Torres')


if __name__ == "__main__":
    main()