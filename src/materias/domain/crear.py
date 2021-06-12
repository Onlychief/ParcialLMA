class CrearMateria():
    def __init__(self, DB):
        self.DB = DB 
    def run(self, name,semestre):
        
        cursor = self.DB.cursor()
        cursor.execute('insert into materias(name,semester) values(%s,%s)', (name, semestre))
        cursor.close()