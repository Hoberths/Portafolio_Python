import tkinter as tk
from tkinter import filedialog, messagebox

# --- Funciones de Lógica de Archivos ---
def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if ruta_archivo:
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                area_texto.delete(1.0, tk.END) # Limpia el texto actual
                area_texto.insert(tk.END, archivo.read()) # Inserta el nuevo contenido
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo:\n{e}")

def guardar_archivo():
    ruta_archivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if ruta_archivo:
        try:
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                # Obtiene todo el texto desde la línea 1, carácter 0 hasta el final
                archivo.write(area_texto.get(1.0, tk.END)) 
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")

# --- Configuración de la Interfaz Gráfica (GUI) ---
# 1. Ventana principal
root = tk.Tk()
root.title("Bloc de Notas en Python")
root.geometry("600x400")

# 2. Barra de menú
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

# 3. Menú "Archivo"
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir...", command=abrir_archivo)
menu_archivo.add_command(label="Guardar como...", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

# 4. Área de texto principal
area_texto = tk.Text(root, font=("Segoe UI", 12))
# expand=True y fill="both" hacen que el cuadro de texto se ajuste si cambias el tamaño de la ventana
area_texto.pack(expand=True, fill="both")

# Iniciar el bucle principal de la aplicación
root.mainloop()