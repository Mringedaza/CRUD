from Conexion import *    

class CClientes:

    def EliminarClientes(Cedula):

        try:
            con = CConexion.conexionBaseDeDatos()
            cursor = con.cursor()
            sql = "Delete from usuarios WHERE usuarios.cedula = %s ;"
            valores = (Cedula,)
            cursor.execute(sql, valores)
            con.commit()
            print(cursor.rowcount, "Registro Eliminado")
            con.close()
        except mysql.connector.Error as error:
            print("Error de eliminacion de datos {}".format(error))

    def modificarClientes(Cedula, Nombre, Apellido, Edad, Sexo):
        try:
            con = CConexion.conexionBaseDeDatos()
            cursor = con.cursor()
            sql = "UPDATE usuarios SET usuarios.Nombre = %s, usuarios.Apellido = %s, usuarios.Edad = %s, usuarios.Sexo = %s WHERE usuarios.cedula = %s;"
            valores = (Nombre, Apellido, Edad, Sexo, Cedula)
            cursor.execute(sql, valores)
            con.commit()
            print(cursor.rowcount, "Registro Actualizado")
            con.close()
        except mysql.connector.Error as error:
            print("Error al actualizar {}".format(error))

    def MostrarClientes():

        try:
            con = CConexion.conexionBaseDeDatos()
            cursor = con.cursor()
            cursor.execute ("select * from usuarios;")
            Resul=cursor.fetchall()
            con.commit()
            con.close()
            return Resul
        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))
      

    def IngresoDeClientes(Cedula, Nombre, Apellido, Edad, Sexo):

        try:
            con = CConexion.conexionBaseDeDatos()
            cursor = con.cursor()
            sql = "insert into usuarios values(%s, %s, %s, %s, %s);"
            valores = (Cedula, Nombre, Apellido, Edad, Sexo)
            cursor.execute(sql, valores)
            con.commit()
            print(cursor.rowcount, "Registro Ingresado")
            con.close()
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))