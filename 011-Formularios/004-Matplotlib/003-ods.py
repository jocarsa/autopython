import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo .ods (ajusta el nombre si es necesario)
df = pd.read_excel("paises.ods", engine="odf")

# Eliminar filas vacías si las hubiera
df = df.dropna()

# Obtener etiquetas y valores
labels = df["Pais"]
sizes = df["Dato"]

# Crear el gráfico de pastel
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Distribución por país")
plt.axis('equal')  # Mantiene el círculo proporcional
plt.show()
