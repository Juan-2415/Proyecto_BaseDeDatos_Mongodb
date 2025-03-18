from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['biblioteca']

# Menú de navegación
@app.route('/')
def index():
    return render_template('index.html')

# CRUD para Usuario
@app.route('/usuario')
def usuario():
    usuarios = list(db.usuario.find())
    return render_template('usuario.html', usuarios=usuarios)

@app.route('/add_usuario', methods=['POST'])
def add_usuario():
    nombre = request.form['nombre']
    db.usuario.insert_one({'nombre': nombre})
    return redirect(url_for('usuario'))

@app.route('/update_usuario/<id>', methods=['POST'])
def update_usuario(id):
    nombre = request.form['nombre']
    db.usuario.update_one({'_id': ObjectId(id)}, {'$set': {'nombre': nombre}})
    return redirect(url_for('usuario'))

@app.route('/delete_usuario/<id>')
def delete_usuario(id):
    db.usuario.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('usuario'))

# CRUD para Libro
@app.route('/libro')
def libro():
    libros = list(db.libro.find())
    return render_template('libro.html', libros=libros)

@app.route('/add_libro', methods=['POST'])
def add_libro():
    titulo = request.form['titulo']
    autor = request.form['autor']
    db.libro.insert_one({'titulo': titulo, 'autor': autor})
    return redirect(url_for('libro'))

@app.route('/update_libro/<id>', methods=['POST'])
def update_libro(id):
    titulo = request.form['titulo']
    autor = request.form['autor']
    db.libro.update_one({'_id': ObjectId(id)}, {'$set': {'titulo': titulo, 'autor': autor}})
    return redirect(url_for('libro'))

@app.route('/delete_libro/<id>')
def delete_libro(id):
    db.libro.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('libro'))

# CRUD para Ejemplar
@app.route('/ejemplar')
def ejemplar():
    ejemplares = list(db.ejemplar.find())
    return render_template('ejemplar.html', ejemplares=ejemplares)

@app.route('/add_ejemplar', methods=['POST'])
def add_ejemplar():
    codigo = request.form['codigo']
    estado = request.form['estado']
    db.ejemplar.insert_one({'codigo': codigo, 'estado': estado})
    return redirect(url_for('ejemplar'))

@app.route('/update_ejemplar/<id>', methods=['POST'])
def update_ejemplar(id):
    codigo = request.form['codigo']
    estado = request.form['estado']
    db.ejemplar.update_one({'_id': ObjectId(id)}, {'$set': {'codigo': codigo, 'estado': estado}})
    return redirect(url_for('ejemplar'))

@app.route('/delete_ejemplar/<id>')
def delete_ejemplar(id):
    db.ejemplar.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('ejemplar'))

# CRUD para Reserva
@app.route('/reserva')
def reserva():
    reservas = list(db.reserva.find())
    return render_template('reserva.html', reservas=reservas)

@app.route('/add_reserva', methods=['POST'])
def add_reserva():
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    fecha = request.form['fecha']
    db.reserva.insert_one({'usuario_id': usuario_id, 'libro_id': libro_id, 'fecha': fecha})
    return redirect(url_for('reserva'))

@app.route('/update_reserva/<id>', methods=['POST'])
def update_reserva(id):
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    fecha = request.form['fecha']
    db.reserva.update_one({'_id': ObjectId(id)}, {'$set': {'usuario_id': usuario_id, 'libro_id': libro_id, 'fecha': fecha}})
    return redirect(url_for('reserva'))

@app.route('/delete_reserva/<id>')
def delete_reserva(id):
    db.reserva.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('reserva'))

# CRUD para Préstamo
@app.route('/prestamo')
def prestamo():
    prestamos = list(db.prestamo.find())
    return render_template('prestamo.html', prestamos=prestamos)

@app.route('/add_prestamo', methods=['POST'])
def add_prestamo():
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    fecha_prestamo = request.form['fecha_prestamo']
    fecha_devolucion = request.form['fecha_devolucion']
    db.prestamo.insert_one({'usuario_id': usuario_id, 'libro_id': libro_id, 'fecha_prestamo': fecha_prestamo, 'fecha_devolucion': fecha_devolucion})
    return redirect(url_for('prestamo'))

@app.route('/update_prestamo/<id>', methods=['POST'])
def update_prestamo(id):
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    fecha_prestamo = request.form['fecha_prestamo']
    fecha_devolucion = request.form['fecha_devolucion']
    db.prestamo.update_one({'_id': ObjectId(id)}, {'$set': {'usuario_id': usuario_id, 'libro_id': libro_id, 'fecha_prestamo': fecha_prestamo, 'fecha_devolucion': fecha_devolucion}})
    return redirect(url_for('prestamo'))

@app.route('/delete_prestamo/<id>')
def delete_prestamo(id):
    db.prestamo.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('prestamo'))

# CRUD para Historial
@app.route('/historial')
def historial():
    historiales = list(db.historial.find())
    return render_template('historial.html', historiales=historiales)

@app.route('/add_historial', methods=['POST'])
def add_historial():
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    accion = request.form['accion']
    fecha = request.form['fecha']
    db.historial.insert_one({'usuario_id': usuario_id, 'libro_id': libro_id, 'accion': accion, 'fecha': fecha})
    return redirect(url_for('historial'))

@app.route('/update_historial/<id>', methods=['POST'])
def update_historial(id):
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    accion = request.form['accion']
    fecha = request.form['fecha']
    db.historial.update_one({'_id': ObjectId(id)}, {'$set': {'usuario_id': usuario_id, 'libro_id': libro_id, 'accion': accion, 'fecha': fecha}})
    return redirect(url_for('historial'))

@app.route('/delete_historial/<id>')
def delete_historial(id):
    db.historial.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('historial'))

if __name__ == '__main__':
    app.run(debug=True)