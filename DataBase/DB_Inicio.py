import sqlite3

def consulta(correo, password):
    db=sqlite3.connect('Mensajes.s3db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    consulta = "select * from Usuarios where CorreoUsuario\
         = '" + correo + "' and Password = '" + password + \
            "' and Estado = '1'"
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado


def manipulacion():
    db=sqlite3.connect('Mensajes.s3db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    consulta = "insert into Usuarios (NombreUsuario, \
        CorreoUsuario, Password, Estado, CodigoActivacion)\
             values ('"+ Usuario +"','" + correo + "','" \
                + password + "','0','"+ codigo +"')"
    cursor.execute(consulta)
    db.commit()
    return "1"


def main():
    consulta('David','david@usbbog.edu.co','123456','1')
    manipulacion()


if __name__ == "__main__":
    main()