from flask import Flask, render_template, request, redirect, flash
import sqlite3
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cambiar por una clave segura

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS inscripciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            dia TEXT NOT NULL,
            hora TEXT NOT NULL,
            fecha_inscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def validar_email(email):
    """Valida formato de email"""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def verificar_disponibilidad(dia, hora):
    """Verifica si hay cupo disponible (máximo 10 personas por clase)"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM inscripciones WHERE dia = ? AND hora = ?', (dia, hora))
    count = c.fetchone()[0]
    conn.close()
    return count < 10

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/horarios')
def schedule():
    return render_template('schedule.html')

@app.route('/inscribirse', methods=['POST'])
def inscribirse():
    nombre = request.form.get('nombre', '').strip()
    email = request.form.get('email', '').strip()
    dia = request.form.get('dia', '')
    hora = request.form.get('hora', '')

    # Validaciones
    if not nombre or not email or not dia or not hora:
        flash('Todos los campos son obligatorios', 'error')
        return redirect('/')
    
    if not validar_email(email):
        flash('El formato del email no es válido', 'error')
        return redirect('/')
    
    if not verificar_disponibilidad(dia, hora):
        flash(f'No hay cupos disponibles para {dia} a las {hora}', 'error')
        return redirect('/')

    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        # Verificar si ya existe una inscripción con el mismo email para el mismo día y hora
        c.execute('SELECT * FROM inscripciones WHERE email = ? AND dia = ? AND hora = ?', 
                  (email, dia, hora))
        if c.fetchone():
            flash('Ya estás inscrito en esta clase', 'warning')
            conn.close()
            return redirect('/')
        
        c.execute('INSERT INTO inscripciones (nombre, email, dia, hora) VALUES (?, ?, ?, ?)',
                  (nombre, email, dia, hora))
        conn.commit()
        conn.close()
        
        flash(f'¡Inscripción exitosa! Te esperamos el {dia} a las {hora}', 'success')
        return render_template('success.html', nombre=nombre)
        
    except sqlite3.Error as e:
        flash('Error en la base de datos. Intenta nuevamente.', 'error')
        return redirect('/')

@app.route('/admin')
def admin():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM inscripciones ORDER BY fecha_inscripcion DESC')
    inscripciones = c.fetchall()
    conn.close()
    return render_template('admin.html', inscripciones=inscripciones)

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_inscripcion(id):
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('DELETE FROM inscripciones WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        flash('Inscripción eliminada exitosamente', 'success')
    except sqlite3.Error as e:
        flash('Error al eliminar la inscripción', 'error')
    
    return redirect('/admin')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
