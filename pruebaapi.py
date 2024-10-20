import requests

# URL de la API
url = "https://api.deliverygoperu.com/establecimiento.php"

# Datos a enviar
payload = {
    "token": "2342423423423",
    "query": "tu_busqueda_aqui"  # Cambia esto por el término que quieras buscar
}

# Hacer la solicitud POST
try:
    response = requests.post(url, json=payload)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Imprimir los datos devueltos por la API
        data = response.json()
        print("Resultados de la búsqueda:", data)
    else:
        print("Error en la solicitud:", response.status_code, response.text)

except requests.exceptions.RequestException as e:
    print("Error de conexión:", e)
