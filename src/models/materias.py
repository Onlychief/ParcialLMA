from src.config.db import mysql


class MateriasModel():
    def agregar_materia(self, name, semester):
        cursor = mysql.get_db().cursor()

        cursor.execute('insert into materias(name,semester) values(%s,%s)', (name, semester))
        mysql.get_db().commit()
        cursor.close()
    
    def mostrar_materias(self):
        cursor = mysql.get_db().cursor()
        cursor.execute('select * from materias')
        data = cursor.fetchall()
        cursor.close()
        return data