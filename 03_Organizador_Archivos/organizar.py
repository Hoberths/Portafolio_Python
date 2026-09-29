from pathlib import Path

# Mantenemos la carpeta de prueba por ahora
carpeta_objetivo = Path("Prueba_Descargas")

if not carpeta_objetivo.exists():
    carpeta_objetivo.mkdir()
    print(f"📁 Se creó la carpeta de prueba: {carpeta_objetivo.absolute()}")

# Definir categorías de extensiones 
categorias = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"]
}

# Diccionario invertido para búsquedas rápidas
extension_a_categoria = {}
for categoria, exts in categorias.items():
    for ext in exts:
        extension_a_categoria[ext.lower()] = categoria

# Listar y Mover 
# Listamos solo los archivos (ignorando carpetas existentes)
archivos = [f for f in carpeta_objetivo.iterdir() if f.is_file()]

for archivo in archivos:
    # Medida de seguridad: evitar mover el propio script
    if archivo.name == "organizar.py":
        continue

    # Obtenemos la extensión en minúsculas y buscamos su categoría
    ext = archivo.suffix.lower()
    categoria = extension_a_categoria.get(ext, "Otros")
    
    # Preparamos la ruta de destino y creamos la carpeta si no existe
    destino_dir = carpeta_objetivo / categoria
    destino_dir.mkdir(exist_ok=True)
    
    # Movemos el archivo
    archivo.rename(destino_dir / archivo.name)
    print(f"✅ Movido '{archivo.name}' a la carpeta '{categoria}/'")

print("🚀 Organización completada.")