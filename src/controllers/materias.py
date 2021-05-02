from flask import render_template, request, redirect, url_for,flash
from src import app
from src.models.materias import MateriasModel
from src.config.db import mysql

app.secret_key = "mysecretkey"

@app.route('/materias')
def materias():
    materiasModel = MateriasModel()

    materias = materiasModel.mostrar_materias()
   
    return render_template('estudiantes/materias.html', materias = materias)

@app.route('/estudiantes/crear_materias', methods =['GET', 'POST'])
def agregar_materia():
   #esta funcion me sirve para mostrar el formulario de creacion
   #y tambien me sirve para crear un nuevo producto
   #estos pasos se identifican con los metodos 
    if request.method == 'GET':
       #mostramos el formulario de creacion
        return render_template('estudiantes/crear_materias.html')

    
    name = request.form.get('name')
    semester = request.form.get('semester')
    materiasModel = MateriasModel()
    materiasModel.agregar_materia(name, semester)
    


    return redirect(url_for('materias'))

@app.route('/editm/<id>', methods = ['POST', 'GET'])
def get_materia(id):
    cur = mysql.get_db().cursor()
    cur.execute("SELECT * FROM materias WHERE id=%s",(id,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('estudiantes/actualizar_materia.html', materia = data[0])


@app.route('/updatem/<id>', methods=['POST'])
def update_materia(id):
    if request.method == 'POST':
        materia = request.form['name']
        semester = request.form['semester']
        cur = mysql.get_db().cursor()
        cur.execute("""
            UPDATE materias
            SET name = %s,
                semester = %s
            WHERE id = %s
        """, (materia, semester, id))
        flash('Operacion ¡Exitosa!')
        mysql.get_db().commit()
        return redirect(url_for('materias'))

@app.route('/deletem/<string:id>', methods = ['POST','GET'])
def delete_materia(id):
    cur = mysql.get_db().cursor()
    cur.execute('DELETE FROM materias WHERE id = {0}'.format(id))
    mysql.get_db().commit()
    flash('Asignatura Eliminada Satisfactoriamente')
    return redirect(url_for('materias'))