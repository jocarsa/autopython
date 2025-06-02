import yfinance as yf
import pandas as pd

# Configurar pandas para mostrar todo el DataFrame
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

# Crear un objeto Ticker para Apple
apple = yf.Ticker("AAPL")

# Obtener información histórica del último año
data = apple.history(period="1y")

# Mostrar todos los datos si están disponibles
if not data.empty:
    print(data)
else:
    print("No se pudo obtener la cotización.")
