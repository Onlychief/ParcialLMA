from src.materias.domain.listarid import ListarMateriasId

class ListarMateriaIdCase:
    def __init__(self, DB):
        self.DB = DB
    def run (self,id):
        listarMateriasId = ListarMateriasId(self.DB)
        data = listarMateriasId.run(id)
        return (data)


