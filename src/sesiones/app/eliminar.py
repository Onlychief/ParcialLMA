from flask import render_template, request, redirect, url_for, flash
from src.sesiones.domain.eliminar import EliminarSesion

class EliminarSesionCase:
    def __init__(self, DB):
        self.DB = DB
    def run(self,id):
        eliminarSesion = EliminarSesion(self.DB)
        eliminarSesion.run(id)