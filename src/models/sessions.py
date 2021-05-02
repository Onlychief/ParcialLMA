from src.config.db import mysql


class SessionModel():
    def agregar_sesion(self, materia, fecha, hora_ini, hora_fin, asistencia):
        cursor = mysql.get_db().cursor()

        cursor.execute('insert into session(materia, fecha, hora_ini, hora_fin, asistencia) values(%s,%s,%s,%s,%s)', (materia, fecha, hora_ini, hora_fin, asistencia))
        mysql.get_db().commit()
        cursor.close()
    
    def mostrar_session(self):
        cursor = mysql.get_db().cursor()
        cursor.execute('select * from session')
        data = cursor.fetchall()
        cursor.close()
        return data
    
    def editar_session(self, id):
        cur = mysql.get_db().cursor()
        cur.execute("SELECT * FROM session WHERE id=%s",(id,))
        data = cur.fetchall()
        cur.close()
        return data
    
    def update_session(self, materia, fecha, hora_ini, hora_fin, asistencia, id):
        cur = mysql.get_db().cursor()
        cur.execute("""
            UPDATE session
            SET materia = %s,
                fecha = %s,
                hora_ini = %s,
                hora_fin = %s,
                asistencia = %s
                
            WHERE id = %s
        """, (materia, fecha, hora_ini, hora_fin, asistencia, id))
        mysql.get_db().commit()