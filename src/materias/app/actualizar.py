from flask import render_template, request, redirect, url_for, flash
from src.materias.domain.actualizar import ActualizarMateria

class ActualizarMateriaCase:
    def __init__(self, DB):
        self.DB = DB
    def run(self,id):

        materia = request.form['name']
        semester = request.form['semester']

        actualizarEstudiante = ActualizarMateria(self.DB)
    
        actualizarEstudiante.run(materia,semester,id)