from src.materias.domain.listar import ListarMateria

class ListarMateriaCase:
    def __init__(self, DB):
        self.DB = DB
    def run (self):
        listarMaterias = ListarMateria(self.DB)
        return (listarMaterias.run())


