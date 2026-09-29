# Organizador Automático de Archivos 📂

Script de automatización diseñado para la optimización de procesos operativos. Su función es escanear un directorio desordenado y clasificar los archivos masivamente en subcarpetas según su formato o extensión, sin intervención humana.

## 🛠️ Conceptos Aplicados
* **Interacción con el OS:** Uso de la librería nativa `pathlib` para la gestión segura de rutas de archivos, independientemente del sistema operativo (Windows, Mac, Linux).
* **Estructuras de Datos eficientes:** Implementación de un diccionario invertido para mapear rápidamente extensiones con su categoría de destino.
* **Manejo de Excepciones:** Lógica preventiva (mediante `exist_ok=True` y `.is_file()`) para evitar sobreescritura de datos o errores al crear directorios que ya existen.

## 🚀 Cómo probarlo
1. Coloca archivos desordenados en la carpeta objetivo definida en el código.
2. Ejecuta el script:
   ```bash
   python organizar.py