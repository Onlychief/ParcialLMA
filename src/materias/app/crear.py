from flask import render_template, request, redirect, url_for, flash
from src.materias.domain.crear import CrearMateria

class CrearMateriaCase:
    def __init__(self, DB):
        self.DB = DB
    def run(self):
        name = request.form.get('name')
        semester = request.form.get('semester')
        
        crearMateria = CrearMateria(self.DB)
        crearMateria.run(name, semester)
        


 
 