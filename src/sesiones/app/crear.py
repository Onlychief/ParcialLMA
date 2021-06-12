from flask import render_template, request, redirect, url_for, flash
from src.sesiones.domain.crear import CrearSesion


class CrearSesionCase:
    def __init__(self, DB):
        self.DB = DB
    def run(self):
        materia = request.form.get('materia')
        fecha = request.form.get('fecha')
        hora_ini = request.form.get('hora_ini')
        hora_fin = request.form.get('hora_fin')
        asistencia = request.form.get('asistencia')

        sessionModel = CrearSesion(self.DB)
        sessionModel.run(materia, fecha, hora_ini, hora_fin, asistencia)
        
        



    


