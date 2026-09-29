# Gestor de Tareas Web (CRUD) 🌐

Esta aplicación web demuestra la implementación de una arquitectura **Cliente-Servidor** utilizando **Flask**. Permite gestionar tareas diarias mediante operaciones CRUD (Crear, Leer, Actualizar, Borrar) directamente desde el navegador.

## ⚙️ Características y Lógica Técnica
* **Routing y Controladores:** Manejo de peticiones HTTP (GET y POST) para renderizar vistas y procesar datos de formularios.
* **Persistencia de Datos:** Lectura y escritura dinámica en un archivo `tareas.json`, simulando el comportamiento de una base de datos NoSQL.
* **Motor de Plantillas:** Uso de Jinja2 para inyectar datos del backend al frontend (HTML) de manera dinámica.

## 🚀 Cómo ejecutar localmente
1. Abre tu terminal en esta carpeta.
2. Ejecuta el servidor de desarrollo de Flask:
   ```bash
   python app.py