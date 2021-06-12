from flask import render_template, request, redirect, url_for, flash
from src.estudiantes.domain.eliminar import EliminarEstudiante


class EliminarAlumnoCase:
    def __init__(self, DB):
        self.DB = DB
    def run(self,id):
        eliminarEstudiante = EliminarEstudiante(self.DB)
        eliminarEstudiante.run(id)
        