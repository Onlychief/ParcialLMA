from flask import render_template, request, redirect, url_for, flash
from src.sesiones.domain.actualizar import ActualizarSesion

class ActualizarSesionCase:
    def __init__(self, DB):
        self.DB = DB   
    def run(self,id):
        materia = request.form['materia']
        fecha = request.form['fecha']
        hora_ini = request.form['hora_ini']
        hora_fin = request.form['hora_fin']
        asistencia = request.form['asistencia']
        updateModel = ActualizarSesion(self.DB)
        updateModel.run(materia, fecha, hora_ini,hora_fin, asistencia, id)