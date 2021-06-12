from flask import render_template, request, redirect, url_for, flash
from src.estudiantes.domain.crear import CrearEstudiante


class CrearAlumnoCase:
    def __init__(self, DB):
        self.DB = DB
    def run(self):
        cc = request.form.get('cc')
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        celular = request.form.get('celular')
        email = request.form.get('email')
        semestre = request.form.get('semestre')
        materia = request.form.get('materia')
        crearEstudiante = CrearEstudiante(self.DB)
        crearEstudiante.run(cc, nombre, apellido, celular, email, semestre,materia)
        


 
