from plotnine import ggplot, aes, geom_point, labs
import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [3, 7, 8, 5, 9],
    'categoria': ['A', 'B', 'A', 'B', 'A']
})

# Crear el gráfico
grafico = (
    ggplot(df, aes(x='x', y='y', color='categoria')) +
    geom_point(size=4) +
    labs(title='Ejemplo de ggplot', x='Eje X', y='Eje Y')
)

# Mostrar usando matplotlib
fig = grafico.draw()

plt.show()
