from src.config.db import mysql


class AlumnoModel():
    def agregar_alumno(self, cc, nombre, apellido, celular, email, semestre,materia):
        cursor = mysql.get_db().cursor()

        cursor.execute('insert into estudiante(cc, nombre, apellido, celular, email, semestre,materia) values(%s,%s,%s,%s,%s,%s,%s)', (cc, nombre, apellido, celular, email, semestre,materia))
        mysql.get_db().commit()
        cursor.close()
    
    def mostrar_estudiantes(self):
        cursor = mysql.get_db().cursor()
        cursor.execute('select * from estudiante')
        data = cursor.fetchall()
        cursor.close()
        return data
    def editar_estudiante(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("select * from estudiante WHERE id=%s",(id,))
        data = cursor.fetchone()
        cursor.close()
        return data

    def update_estudiante(self, cc, nombre, apellido, celular, email, semestre,id):
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE estudiante
            SET cc = %s,
                nombre = %s,
                apellido = %s,
                celular = %s,
                email = %s,
                semester = %s
            WHERE id = %s
        """, (cc, nombre, apellido, celular, email, semestre,id))
        mysql.connection.commit()
        cur.close()

    
