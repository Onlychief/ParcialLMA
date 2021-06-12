class ListarSesionesId():
    def __init__(self, DB):
        self.DB = DB

    def run(self,id):
        cur = self.DB.cursor()
        cur.execute("SELECT * FROM session WHERE id=%s",(id,))
        data = cur.fetchall()
        cur.close()
        return data