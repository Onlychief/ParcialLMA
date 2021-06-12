class ActualizarEstudiante():
    def __init__(self, DB):
        self.DB = DB
    def run(self,cc, nombre, apellido, celular, email, semestre,id):
        cur = self.DB.cursor()
        cur.execute("""
            UPDATE estudiante
            SET cc = ?,
                nombre = ?,
                apellido = ?,
                email = ?,
                celular = ?,
                semestre = ?
            WHERE id = ?
        """, (cc, nombre, apellido, email, celular, semestre, id))
        cur.close()
        