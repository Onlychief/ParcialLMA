class ListarMateriasId():
    def __init__(self, DB):
        self.DB = DB

    def run(self,id):
        cursor = self.DB.cursor()
        cursor.execute('select * from materias where id=?', [id])
        data = cursor.fetchall()
        return (data)