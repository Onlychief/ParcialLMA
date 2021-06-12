from src.sesiones.domain.listar import ListarSesiones

class ListarSesionesCase:
    def __init__(self, DB):
        self.DB = DB
    def run (self):

        listarSesiones = ListarSesiones(self.DB)
        return (listarSesiones.run())




