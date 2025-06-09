import plotly.express as px

# Datos de ejemplo jerárquicos
data = dict(
    character=["Eddard", "Catelyn", "Robb", "Sansa", "Arya", "Bran", "Rickon"],
    parent=["", "Eddard", "Catelyn", "Catelyn", "Catelyn", "Catelyn", "Catelyn"],
    value=[10, 14, 12, 10, 8, 6, 4]
)

fig = px.sunburst(data, names='character', parents='parent', values='value')
fig.show()  # Abre en navegador automáticamente
