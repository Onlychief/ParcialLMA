from flask import render_template, request, redirect, url_for, flash
from src.materias.domain.eliminar import EliminarMateria

class EliminarMateriaCase:
    def __init__(self, DB):
        self.DB = DB
    def run(self,id):
        
        eliminarMateria = EliminarMateria(self.DB)
        eliminarMateria.run(id)
        

