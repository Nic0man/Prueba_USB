import sqlite3
#http://rogercorp.club/minticc3/

def validar(usuario):
    db=sqlite3.connect("datos.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select * from Usuarios where apellido='" + usuario +"'"
    #consulta="select * from Usuarios"
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

def validar2(usuario):
    db=sqlite3.connect("datos.s3db")
    db.row_factory=sqlite3.Row
    cursor=db.cursor()
    consulta="select * from Usuarios where apellido = '" + usuario +"'"
    cursor.execute(consulta)
    resultado=cursor.fetchone()
    print(list(resultado))
    # for i in resultado:
    #     print(i)
    
    cursor.close()
    db.close()
    return resultado

def Registrar(nombre,apellido,edad):
    db = sqlite3.connect("datos.s3db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    consulta = "insert into Usuarios (nombre,apellido,edad) values ('"+ nombre +"','" + apellido + "'," + str(edad) +")"
    cursor.execute(consulta)
    db.commit()
    cursor.close()
    db.close()
    return "1"


def main():
    #Registrar('Alfredo','Torres',62)
    validar('Torres')
    validar2('Torres')


if __name__ == "__main__":
    main()