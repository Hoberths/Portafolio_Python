# Editor de Notas (Desktop GUI) 📝

Aplicación de escritorio interactiva construida con la librería estándar **Tkinter**. Este proyecto representa la transición hacia la **Programación Orientada a Objetos (POO)** y la arquitectura dirigida por eventos (*Event-Driven Programming*).

## ✨ Funcionalidades
* Interfaz gráfica nativa con área de texto multilínea expandible.
* Menú superior con opciones integradas del sistema para Abrir y Guardar archivos (`filedialog`).
* Alertas y manejo de errores visibles al usuario a través de ventanas modales (`messagebox`).

## 🧠 Arquitectura de Software
Todo el código está encapsulado en una clase `EditorNotas` que hereda de `tk.Tk`. Esto hace que el código sea modular, escalable y mantenga un estado limpio, permitiendo agregar nuevas ventanas o funciones en el futuro sin romper la lógica existente.

## 🚀 Cómo abrir la aplicación
1. En tu terminal, asegúrate de estar en este directorio.
2. Levanta la interfaz gráfica con:
   ```bash
   python bloc_notas.py