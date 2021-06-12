class ActualizarSesion():
    def __init__(self, DB):
        self.DB = DB
    def run(self, materia, fecha, hora_ini,hora_fin, asistencia, id):
        cur = self.DB.cursor()
        cur.execute("""
            UPDATE session
            SET materia = ?,
                fecha = ?,
                hora_ini = ?,
                hora_fin = ?,
                asistencia = ?,
            WHERE id = ?
        """, (materia, fecha, hora_ini,hora_fin, asistencia, id))
        cur.close()