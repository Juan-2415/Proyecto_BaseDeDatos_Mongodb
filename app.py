from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuración de la conexión a MySQL
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="juand",          # Cambia por tu usuario de MySQL
            password="juan2415",          # Cambia por tu contraseña (si tienes)
            database="biblioteca"  # Asegúrate de que la BD existe
        )
        return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Rutas principales
@app.route('/')
def index():
    return render_template('index.html')

# ================== USUARIOS ==================
@app.route('/usuario')
def usuario():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()
    connection.close()
    return render_template('usuario.html', usuarios=usuarios)

@app.route('/add_usuario', methods=['POST'])
def add_usuario():
    nombre = request.form['nombre']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO usuario (nombre) VALUES (%s)", (nombre,))
    connection.commit()
    connection.close()
    return redirect(url_for('usuario'))

@app.route('/update_usuario/<int:id>', methods=['POST'])
def update_usuario(id):
    nombre = request.form['nombre']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE usuario SET nombre = %s WHERE id = %s", (nombre, id))
    connection.commit()
    connection.close()
    return redirect(url_for('usuario'))

@app.route('/delete_usuario/<int:id>')
def delete_usuario(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))
    connection.commit()
    connection.close()
    return redirect(url_for('usuario'))

# ================== LIBROS ==================
@app.route('/libro')
def libro():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM libro")
    libros = cursor.fetchall()
    connection.close()
    return render_template('libro.html', libros=libros)

@app.route('/add_libro', methods=['POST'])
def add_libro():
    titulo = request.form['titulo']
    autor = request.form['autor']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO libro (titulo, autor) VALUES (%s, %s)", (titulo, autor))
    connection.commit()
    connection.close()
    return redirect(url_for('libro'))

@app.route('/update_libro/<int:id>', methods=['POST'])
def update_libro(id):
    titulo = request.form['titulo']
    autor = request.form['autor']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE libro SET titulo = %s, autor = %s WHERE id = %s", (titulo, autor, id))
    connection.commit()
    connection.close()
    return redirect(url_for('libro'))

@app.route('/delete_libro/<int:id>')
def delete_libro(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM libro WHERE id = %s", (id,))
    connection.commit()
    connection.close()
    return redirect(url_for('libro'))

# ================== EJEMPLARES ==================
@app.route('/ejemplar')
def ejemplar():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ejemplar")
    ejemplares = cursor.fetchall()
    connection.close()
    return render_template('ejemplar.html', ejemplares=ejemplares)

@app.route('/add_ejemplar', methods=['POST'])
def add_ejemplar():
    codigo = request.form['codigo']
    estado = request.form['estado']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO ejemplar (codigo, estado) VALUES (%s, %s)", (codigo, estado))
    connection.commit()
    connection.close()
    return redirect(url_for('ejemplar'))

@app.route('/update_ejemplar/<int:id>', methods=['POST'])
def update_ejemplar(id):
    codigo = request.form['codigo']
    estado = request.form['estado']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE ejemplar SET codigo = %s, estado = %s WHERE id = %s", (codigo, estado, id))
    connection.commit()
    connection.close()
    return redirect(url_for('ejemplar'))

@app.route('/delete_ejemplar/<int:id>')
def delete_ejemplar(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM ejemplar WHERE id = %s", (id,))
    connection.commit()
    connection.close()
    return redirect(url_for('ejemplar'))

# ================== RESERVAS ==================
@app.route('/reserva')
def reserva():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT r.*, u.nombre as usuario_nombre, l.titulo as libro_titulo 
        FROM reserva r
        JOIN usuario u ON r.usuario_id = u.id
        JOIN libro l ON r.libro_id = l.id
    """)
    reservas = cursor.fetchall()
    connection.close()
    return render_template('reserva.html', reservas=reservas)

@app.route('/add_reserva', methods=['POST'])
def add_reserva():
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    fecha = request.form['fecha']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO reserva (usuario_id, libro_id, fecha) VALUES (%s, %s, %s)", 
            (usuario_id, libro_id, fecha))
    connection.commit()
    connection.close()
    return redirect(url_for('reserva'))

@app.route('/update_reserva/<int:id>', methods=['POST'])
def update_reserva(id):
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    fecha = request.form['fecha']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE reserva 
        SET usuario_id = %s, libro_id = %s, fecha = %s 
        WHERE id = %s
    """, (usuario_id, libro_id, fecha, id))
    connection.commit()
    connection.close()
    return redirect(url_for('reserva'))

@app.route('/delete_reserva/<int:id>')
def delete_reserva(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM reserva WHERE id = %s", (id,))
    connection.commit()
    connection.close()
    return redirect(url_for('reserva'))

# ================== PRÉSTAMOS ==================
@app.route('/prestamo')
def prestamo():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.*, u.nombre as usuario_nombre, l.titulo as libro_titulo 
        FROM prestamo p
        JOIN usuario u ON p.usuario_id = u.id
        JOIN libro l ON p.libro_id = l.id
    """)
    prestamos = cursor.fetchall()
    connection.close()
    return render_template('prestamo.html', prestamos=prestamos)

@app.route('/add_prestamo', methods=['POST'])
def add_prestamo():
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    fecha_prestamo = request.form['fecha_prestamo']
    fecha_devolucion = request.form['fecha_devolucion']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO prestamo (usuario_id, libro_id, fecha_prestamo, fecha_devolucion) 
        VALUES (%s, %s, %s, %s)
    """, (usuario_id, libro_id, fecha_prestamo, fecha_devolucion))
    connection.commit()
    connection.close()
    return redirect(url_for('prestamo'))

@app.route('/update_prestamo/<int:id>', methods=['POST'])
def update_prestamo(id):
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    fecha_prestamo = request.form['fecha_prestamo']
    fecha_devolucion = request.form['fecha_devolucion']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE prestamo 
        SET usuario_id = %s, libro_id = %s, fecha_prestamo = %s, fecha_devolucion = %s
        WHERE id = %s
    """, (usuario_id, libro_id, fecha_prestamo, fecha_devolucion, id))
    connection.commit()
    connection.close()
    return redirect(url_for('prestamo'))

@app.route('/delete_prestamo/<int:id>')
def delete_prestamo(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM prestamo WHERE id = %s", (id,))
    connection.commit()
    connection.close()
    return redirect(url_for('prestamo'))

# ================== HISTORIAL ==================
@app.route('/historial')
def historial():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT h.*, u.nombre as usuario_nombre, l.titulo as libro_titulo 
        FROM historial h
        JOIN usuario u ON h.usuario_id = u.id
        JOIN libro l ON h.libro_id = l.id
    """)
    historiales = cursor.fetchall()
    connection.close()
    return render_template('historial.html', historiales=historiales)

@app.route('/add_historial', methods=['POST'])
def add_historial():
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    accion = request.form['accion']
    fecha = request.form['fecha']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO historial (usuario_id, libro_id, accion, fecha) 
        VALUES (%s, %s, %s, %s)
    """, (usuario_id, libro_id, accion, fecha))
    connection.commit()
    connection.close()
    return redirect(url_for('historial'))

@app.route('/update_historial/<int:id>', methods=['POST'])
def update_historial(id):
    usuario_id = request.form['usuario_id']
    libro_id = request.form['libro_id']
    accion = request.form['accion']
    fecha = request.form['fecha']
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE historial 
        SET usuario_id = %s, libro_id = %s, accion = %s, fecha = %s
        WHERE id = %s
    """, (usuario_id, libro_id, accion, fecha, id))
    connection.commit()
    connection.close()
    return redirect(url_for('historial'))

@app.route('/delete_historial/<int:id>')
def delete_historial(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM historial WHERE id = %s", (id,))
    connection.commit()
    connection.close()
    return redirect(url_for('historial'))

if __name__ == '__main__':
    app.run(debug=True)