from flask import render_template, request, redirect, url_for,flash
from src import app
from src.models.sessions import SessionModel
from src.models.materias import MateriasModel
from src.config.db import mysql

app.secret_key = "mysecretkey"

@app.route('/sessiones')
def sessiones():
    sessionModel = SessionModel()
    session = sessionModel.mostrar_session()
       
    return render_template('sessiones/index.html', session = session)


@app.route('/sessiones/crear', methods =['GET', 'POST'])
def agregar_session():
   #esta funcion me sirve para mostrar el formulario de creacion
   #y tambien me sirve para crear un nuevo producto
   #estos pasos se identifican con los metodos 
    if request.method == 'GET':
       #mostramos el formulario de creacion
        materiasModel = MateriasModel()
        materia2 = materiasModel.mostrar_materias()
        return render_template('sessiones/crear.html', data=materia2)

    
    materia = request.form.get('materia')
    fecha = request.form.get('fecha')
    hora_ini = request.form.get('hora_ini')
    hora_fin = request.form.get('hora_fin')
    asistencia = request.form.get('asistencia')
    sessionModel = SessionModel()
    sessionModel.agregar_sesion(materia, fecha, hora_ini, hora_fin, asistencia)
    
    return redirect(url_for('sessiones'))

@app.route('/edits/<id>', methods = ['POST', 'GET'])
def get_session():
    sessionModel = SessionModel()
    session = sessionModel.editar_session()
    return render_template('sessiones/update.html', data=session[0])


@app.route('/actualizar/<id>', methods=['POST'])
def update_session(id):
    if request.method == 'POST':
        materia = request.form['materia']
        fecha = request.form['fecha']
        hora_ini = request.form['hora_ini']
        hora_fin = request.form['hora_fin']
        
        updateModel = SessionModel()
        update = updateModel.update_session()
        
        flash('Operacion ¡Exitosa!')
        return redirect(url_for('sessiones'))

