import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import requests

load_dotenv()


'''
/*
 * EJERCICIO:
 * Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
 * ¡Dos de las bandas más grandes de la historia están de vuelta!
 * Desarrolla un programa que se conecte al API de Spotify y los compare.
 * Requisitos:
 * 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
 * 2. Conéctate al API utilizando tu lenguaje de programación.
 * 3. Recupera datos de los endpoint que tú quieras.
 * Acciones:
 * 1. Accede a las estadísticas de las dos bandas.
 *    Por ejemplo: número total de seguidores, escuchas mensuales,
 *    canción con más reproducciones...
 * 2. Compara los resultados de, por lo menos, 3 endpoint.
 * 3. Muestra todos los resultados por consola para notificar al usuario.
 * 4. Desarrolla un criterio para seleccionar qué banda es más popular.
 */

'''



# Configura tus credenciales
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

# Autenticación automática
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
)



# Buscar un artista
results = sp.search(q="The Beatles", type="artist", limit=1)
#results_id = sp.search(q="The Beatles", type="artist", limit=1)


print(results)

artist = results["artists"]["items"][0]

artist_id = results['artists']['items'][0]['id']

print(artist_id)

# Ejemplo con Spotipy
# Intenta especificar el límite explícitamente (máximo es 50)
# Asegúrate de que artist_id sea solo el texto del ID

print(artist)
#print(albums)


print(f"Artista: {artist['name']}")
print(f"id: {artist_id}")


# Asegúrate de que artist_id sea solo el texto del ID
# Obtenemos el token del objeto sp que ya tienes creado
token = sp.auth_manager.get_access_token(as_dict=False)
print('---------token-----------------')
print(token)

url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
headers = {"Authorization": f"Bearer {token}"}
params = {"limit": 1}# Probamos con un límite muy bajo

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    print("¡Éxito!")
    for item in response.json()['items']:
        print(item['popularity'])
else:
    print(f"Error {response.status_code}: {response.text}")


#print(f"Seguidores: {artist['followers']['total']:,}")
#print(f"Popularidad: {artist['popularity']}/100")
#print(f"Géneros: {', '.join(artist['genres'])}")
