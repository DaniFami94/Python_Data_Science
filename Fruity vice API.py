import pandas as pd
import requests
import json

url = "https://www.fruityvice.com/api/fruit/all"
data = requests.get(url)

# Verifica el estado de la respuesta
if data.status_code == 200:
    print("Conexión exitosa")

    # Verifica el contenido de la respuesta
    print(data.text)  # Imprime el texto de la respuesta para ver si es válido

    # Si todo está bien, continua con la decodificación
    results = json.loads(data.text)

    # Convertir a DataFrame
    df2 = pd.json_normalize(results)
    print(df2)

    # Filtrar datos de 'Cherry'
    cherry = df2.loc[df2["name"] == 'Cherry']
    print(cherry.iloc[0]['family'], cherry.iloc[0]['genus'])
else:
    print(f"Error en la conexión: {data.status_code}")
