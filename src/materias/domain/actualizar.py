class ActualizarMateria():
    def __init__(self, DB):
        self.DB = DB 
    def run(self, materia, semester, id):
        cur = self.DB.cursor()
        cur.execute("""
            UPDATE materias
            SET name = %s,
                semester = %s
            WHERE id = %s
        """, (materia, semester, id))
        cur.close()