from src.sesiones.domain.listarid import ListarSesionesId

class ListarSesionIdCase:
    def __init__(self, DB):
        self.DB = DB
    def run (self,id):
        listarSesionesId = ListarSesionesId(self.DB)
        data = listarSesionesId.run(id)
        return (data)

