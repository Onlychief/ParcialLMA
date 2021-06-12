from src.sesiones.domain.listara import ListarSesionesA

class AsistenciaCase:
    def __init__(self, DB):
        self.DB = DB
    def run (self):

        listarSesionesa = ListarSesionesA(self.DB)
        return (listarSesionesa.run())

