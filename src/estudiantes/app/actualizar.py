from flask import render_template, request, redirect, url_for, flash
from src.estudiantes.domain.actualizar import ActualizarEstudiante

class ActualizarAlumnoCase:
    def __init__(self, DB):
        self.DB = DB
    def run(self,id):

        cc = request.form['cc']
        fullname = request.form['nombre']
        lastname = request.form['apellido']
        phone = request.form['celular']
        email = request.form['email']
        semester = request.form['semestre']
        materia = request.form['materia']

        actualizarEstudiante = ActualizarEstudiante(self.DB)
        actualizarEstudiante.run(cc,fullname,lastname,phone,email,semester,id)