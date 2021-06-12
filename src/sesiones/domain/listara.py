class ListarSesionesA():
    def __init__(self, DB):
        self.DB = DB

    def run(self):
        cursor = self.DB.cursor()
        cursor.execute('select id,cc,nombre,apellido,semestre from estudiante')
        data = cursor.fetchall()
        cursor.close()
        return data