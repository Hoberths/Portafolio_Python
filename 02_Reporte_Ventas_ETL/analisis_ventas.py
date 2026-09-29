import pandas as pd
import matplotlib.pyplot as plt

#Cargamos el archivo
df = pd.read_csv('02_Reporte_Ventas_ETL/ventas.csv')


##Calcular ventas totales por mes
#Transformación la columna fecha a formato datetime de pandas
df['fecha'] = pd.to_datetime(df['fecha'])
# Calcular ingresos (Cantidad * Precio)
df['ingresos'] = df['cantidad vendida'] * df['precio']
# Extraer el mes para la agrupación (formato YYYY-MM)
df['mes'] = df['fecha'].dt.to_period('M')
# Agrupar ingresos totales por mes
ventas_mensuales = df.groupby('mes')['ingresos'].sum()

##Calcular producto más vendido y con más ingresos
ventas_prod = df.groupby('producto').agg({
    'cantidad vendida': 'sum',
    'ingresos': 'sum'
})

# Obtener los nombres de los productos líderes
mas_vendido = ventas_prod['cantidad vendida'].idxmax()
mayor_ingreso = ventas_prod['ingresos'].idxmax()

print("--- REPORTE DE VENTAS ---")
print(f"Producto más vendido en unidades: {mas_vendido} (total: {ventas_prod.loc[mas_vendido, 'cantidad vendida']} unidades)")
print(f"Producto con mayores ingresos: {mayor_ingreso} (total: ${ventas_prod.loc[mayor_ingreso, 'ingresos']:.2f})")

# --- 4. Visualización de Salida ---
# Gráfico 1: Evolución de ventas mensuales
# Convertir el índice Period a string para evitar conflictos con Matplotlib
ventas_mensuales.index = ventas_mensuales.index.astype(str)
plt.figure(figsize=(8, 5))
ax = ventas_mensuales.plot(kind='bar', color='green', edgecolor='black')
# Agregamos las etiquetas de datos con un ligero margen (padding)
plt.bar_label(ax.containers[0], fmt='$%.0f', padding=3)
plt.title("Ventas Totales por Mes")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")
plt.xticks(rotation=0) # Mantiene el texto de los meses en horizontal
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
# Exportar la gráfica como imagen antes de mostrarla en pantalla
plt.savefig("ventas_por_mes.png")
plt.show()

# --- Gráfico 2: Top 5 Productos Más Vendidos ---
# Extraemos los 5 productos principales
top5 = ventas_prod.nlargest(5, 'ingresos')
plt.figure(figsize=(8, 5))
# Generamos el gráfico de barras
barras = plt.bar(top5.index, top5['ingresos'], color='#d9534f', edgecolor='black')
# Agregamos las etiquetas y usamos 'fmt' para darle formato de moneda sin decimales
plt.bar_label(barras, fmt='$%.0f', padding=3)
plt.title("Top 5 Productos por Ingresos")
plt.ylabel("Ingresos ($)")
plt.xlabel("Producto")
# Rotar las etiquetas 45 grados por si los nombres son largos
plt.xticks(rotation=45)
plt.tight_layout()
# Exportar la segunda imagen
plt.savefig("top5_productos.png")
plt.show()