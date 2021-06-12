class CrearEstudiante():
    def __init__(self, DB):
        self.DB = DB

    def run(self,cc, nombre, apellido, celular, email, semestre,materia ):
        cursor = self.DB.cursor()
        cursor.execute('insert into estudiante(cc, nombre, apellido, celular, email, semestre,materia) values(%s,%s,%s,%s,%s,%s,%s)', (cc, nombre, apellido, celular, email, semestre,materia))
        cursor.close()