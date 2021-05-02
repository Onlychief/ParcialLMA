from flask import render_template, request, redirect, url_for, flash
from src import app
from src.models.estudiantes import AlumnoModel
from src.models.materias import MateriasModel
from src.config.db import mysql

app.secret_key = "mysecretkey"

@app.route('/estudiantes', methods=['GET'])
def estudiantes():
    alumnoModel = AlumnoModel()

    alumno = alumnoModel.mostrar_estudiantes()
   
    return render_template('estudiantes/index.html', alumno = alumno)

@app.route('/show_materias', methods =['GET', 'POST'])
def get_materias():
    cur = mysql.get_db().cursor()
    cur.execute("SELECT * FROM materias")
    data = cur.fetchall()
    cur.close()
    
    return render_template('estudiantes/crear.html', alumno2 = data)

@app.route('/estudiantes/crear', methods =['GET', 'POST'])
def agregar_alumno():
   #esta funcion me sirve para mostrar el formulario de creacion
   #y tambien me sirve para crear un nuevo producto
   #estos pasos se identifican con los metodos 
    if request.method == 'GET':
       #mostramos el formulario de creacion
        materiasModel = MateriasModel()
        materia2 = materiasModel.mostrar_materias()
        return render_template('estudiantes/crear.html', data=materia2)

    cc = request.form.get('cc')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    celular = request.form.get('celular')
    email = request.form.get('email')
    semestre = request.form.get('semestre')
    materia = request.form.get('materia')
    alumnoModel = AlumnoModel()
    alumnoModel.agregar_alumno(cc, nombre, apellido, celular, email, semestre,materia)
    return redirect(url_for('estudiantes'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_student(id):
    cur = mysql.get_db().cursor()
    cur.execute("SELECT * FROM estudiante WHERE id=%s",(id,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('estudiantes/actualizar_estudiante.html', alumno = data[0])


@app.route('/update/<id>', methods=['POST'])
def update_estudiante(id):
    if request.method == 'POST':
        cc = request.form['cc']
        fullname = request.form['nombre']
        lastname = request.form['apellido']
        phone = request.form['celular']
        email = request.form['email']
        semester = request.form['semestre']
        materia = request.form['materia']
        cur = mysql.get_db().cursor()
        cur.execute("""
            UPDATE estudiante
            SET cc = %s,
                nombre = %s,
                apellido = %s,
                email = %s,
                celular = %s,
                semestre = %s
            WHERE id = %s
        """, (cc, fullname, lastname, email, phone, semester, id))
        flash('Operacion ¡Exitosa!')
        mysql.get_db().commit()
        return redirect(url_for('estudiantes'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_student(id):
    cur = mysql.get_db().cursor()
    cur.execute('DELETE FROM estudiante WHERE id = {0}'.format(id))
    mysql.get_db().commit()
    flash('Estudiante Eliminado Satisfactoriamente')
    return redirect(url_for('estudiantes'))

#Materias

