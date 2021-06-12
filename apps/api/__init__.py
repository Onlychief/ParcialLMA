from flask import render_template, request, redirect, url_for,Flask, session, flash
from src.shared.infra.db import DB
from src.estudiantes.app.listar import ListarAlumnosCase
from src.estudiantes.app.listarid import ListarAlumnoIdCase
from src.estudiantes.app.crear import CrearAlumnoCase
from src.estudiantes.app.actualizar import ActualizarAlumnoCase
from src.estudiantes.app.eliminar import EliminarAlumnoCase
from src.materias.app.listar import ListarMateriaCase
from src.materias.app.crear import CrearMateriaCase
from src.materias.app.eliminar import EliminarMateriaCase
from src.materias.app.listarid import ListarMateriaIdCase
from src.materias.app.actualizar import ActualizarMateriaCase
from src.sesiones.app.listar import ListarSesionesCase
from src.sesiones.app.crear import CrearSesionCase
from src.sesiones.app.listara import AsistenciaCase
from src.sesiones.app.listarid import ListarSesionIdCase
from src.sesiones.app.actualizar import ActualizarSesionCase
from src.sesiones.app.eliminar import EliminarSesionCase

app = Flask(__name__, template_folder = 'views')
app.secret_key = "mysecretkey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estudiantes', methods=['GET'])
def estudiantes():
    alumnos = ListarAlumnosCase(DB)
    alumno = alumnos.run()
    return render_template('estudiantes/index.html', alumno = alumno)

@app.route('/estudiantes/crear', methods =['GET', 'POST'])
def agregar_alumno():
    if request.method == 'GET':
            materiasModel = ListarMateriaCase(DB)
            materia2 = materiasModel.run()
            return render_template('estudiantes/crear.html', data2=materia2)
    else: 
            crearEstudiante = CrearAlumnoCase(DB)
            crearEstudiante.run()
            return redirect(url_for('estudiantes'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_student(id):
    materiasModel = ListarMateriaCase(DB)
    materia = materiasModel.run()
    listarConId = ListarAlumnoIdCase(DB)
    data = listarConId.run(id)
    return render_template('estudiantes/actualizar_estudiante.html', alumno = data[0], data =materia)

@app.route('/update/<id>', methods=['POST'])
def update_estudiante(id):
    if request.method == 'POST':
        actualizarAlumno = ActualizarAlumnoCase(DB)
        actualizarAlumno.run(id)
        flash('Operacion ¡Exitosa!')
        return redirect(url_for('estudiantes'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_student(id):
    eliminarEstudiante = EliminarAlumnoCase(DB)
    eliminarEstudiante.run(id)
    flash('Estudiante Eliminado Satisfactoriamente')
    return redirect(url_for('estudiantes'))

@app.route('/materias')
def materias():
    materiasModel = ListarMateriaCase(DB)
    materias = materiasModel.run()
    return render_template('estudiantes/materias.html', materias = materias)

@app.route('/estudiantes/crear_materias', methods =['GET', 'POST'])
def agregar_materia():
    if request.method == 'GET':
        return render_template('estudiantes/crear_materias.html')
    else:    
        materiasModel = CrearMateriaCase(DB)
        materiasModel.run()
        return redirect(url_for('materias'))

@app.route('/deletem/<string:id>', methods = ['POST','GET'])
def delete_materia(id):
    eliminarMateria = EliminarMateriaCase(DB)
    eliminarMateria.run(id)
    flash('Asignatura Eliminada Satisfactoriamente')
    return redirect(url_for('materias'))

@app.route('/editm/<id>', methods = ['POST', 'GET'])
def get_materia(id):
    materiasModel = ListarMateriaIdCase(DB)
    materia = materiasModel.run(id)
    return render_template('estudiantes/actualizar_materia.html',  materia = materia[0])

@app.route('/updatem/<id>', methods=['POST'])
def update_materia(id):
    if request.method == 'POST':
        actualizarMateria = ActualizarMateriaCase(DB)
        actualizarMateria.run(id)
        flash('Operacion ¡Exitosa!')  
        return redirect(url_for('materias'))

@app.route('/sessiones')
def sessiones():
    sessionModel = ListarSesionesCase(DB)
    session = sessionModel.run()
    return render_template('sessiones/index.html', session = session)

@app.route('/sessiones/crear', methods =['GET', 'POST'])
def agregar_session():
  
    if request.method == 'GET':
        materiasModel = ListarMateriaCase(DB)
        materia2 = materiasModel.run()
        return render_template('sessiones/crear.html', data=materia2)
    else:
        crearSesion = CrearSesionCase(DB)
        crearSesion.run()
        return redirect(url_for('sessiones'))

@app.route('/asistencia', methods =['GET', 'POST'])
def asistencia():
    asistenciaModel = AsistenciaCase(DB)
    asistencia = asistenciaModel.run()
    return render_template('sessiones/asistencia.html', data=asistencia) 

@app.route('/edits/<id>', methods = ['POST', 'GET'])
def get_session(id):
    sesionModel = ListarSesionIdCase(DB)
    session = sesionModel.run(id)
    return render_template('sessiones/update.html', data=session)

@app.route('/actualizar/<id>', methods=['POST'])
def update_session(id):
    if request.method == 'POST':
        actualizarSesion = ActualizarSesionCase(DB)
        actualizarSesion.run(id)
        flash('Operacion ¡Exitosa!')
        return redirect(url_for('sessiones'))

@app.route('/deletes/<string:id>', methods = ['POST','GET'])
def delete_session(id):
    eliminarSesion = EliminarSesionCase(DB)
    eliminarSesion.run(id)
    flash('Session Eliminada Satisfactoriamente')
    return redirect(url_for('sessiones'))

def create_app_api():
    app.run(debug=True, port=5000)
