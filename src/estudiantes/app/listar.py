from src.estudiantes.domain.listar import ListarEstudiantes

class ListarAlumnosCase:
    def __init__(self, DB):
        self.DB = DB
    def run (self):
        listarEstudiantes = ListarEstudiantes(self.DB)
        return (listarEstudiantes.run())




