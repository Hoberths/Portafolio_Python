import json
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# --- Estructura de datos global ---
tareas = []
siguiente_id = 1
ARCHIVO_JSON = 'tareas.json'

# --- Funciones de Persistencia ---
def cargar_datos():
    global siguiente_id, tareas
    try:
        with open(ARCHIVO_JSON, 'r') as f:
            data = json.load(f)
            tareas = data['tareas']
            siguiente_id = data['siguiente_id']
    except FileNotFoundError:
        # Si es la primera vez que se ejecuta y no hay archivo, pasamos de largo
        pass

def guardar_datos():
    with open(ARCHIVO_JSON, 'w') as f:
        # Volcamos el estado actual de las variables al archivo
        json.dump({'siguiente_id': siguiente_id, 'tareas': tareas}, f)

# --- Funciones de Lógica de Negocio ---
def agregar_tarea(texto):
    global siguiente_id
    tareas.append({'id': siguiente_id, 'texto': texto, 'hecho': False})
    siguiente_id += 1
    guardar_datos()  # Guardamos automáticamente al añadir

def completar_tarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = True
            break
    guardar_datos()  # Guardamos automáticamente al actualizar

# Cargamos el historial apenas arranca la aplicación
cargar_datos()

# --- Rutas Web ---
@app.route('/')
def index():
    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])
    return render_template('index.html', tareas=tareas_ordenadas)

@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect('/')

@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)