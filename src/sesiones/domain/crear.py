class CrearSesion():
    def __init__(self, DB):
        self.DB = DB

    def run(self,materia, fecha, hora_ini, hora_fin, asistencia):       
        cursor = self.DB.cursor()
        cursor.execute('insert into session(materia, fecha, hora_ini, hora_fin, asistencia) values(%s,%s,%s,%s,%s)', (materia, fecha, hora_ini, hora_fin, asistencia))
        cursor.close()