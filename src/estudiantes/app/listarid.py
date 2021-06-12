from src.estudiantes.domain.listarid import ListarEstudiantesId

class ListarAlumnoIdCase:
    def __init__(self, DB):
        self.DB = DB
    def run (self,id):
        listarEstudiantesId = ListarEstudiantesId(self.DB)
        data = listarEstudiantesId.run(id)
        return (data)


