import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json
import os

# Se pregunta el pokemon que desea buscar
if not os.path.exists('pokedex'):
    os.makedirs('pokedex')
url_imagen = None

print("Hola, bienvenido a la pokedex") 
while True:
    pokemon = input("Escribe el nombre de un pokemon: ")
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        print("Pokemon no encontrado")
    else:
        datos = respuesta.json()
        break

print(f"Felicidades, encontramos a {pokemon}\n")

#Mostrar una imagen del pokemon
try: 
    url_imagen = datos["sprites"]["front_default"]
    imagen = Image.open(urlopen(url_imagen))
    plt.title(datos["name"])
    imgplot = plt.imshow(imagen)
    plt.show()
except:
    print("El pokemon no tiene imagen")


#Mostrar peso y tamaño del pokemon

pokepeso = datos["weight"]
pokealtura = datos["height"]
print(f"El peso de {pokemon} es {pokepeso} hectogramos.")
print(f"El peso de {pokemon} es {pokealtura} decigramos.")


#Mostrar movimientos, habilidades y el tipo del pokemon

print("\nMovimientos de " + pokemon + ": ")
movimientos = datos["moves"]
for i in range(int(len(movimientos))):
    movimiento = movimientos[i]["move"]["name"]
    print(f"{i + 1}. {movimiento}")

print("\nHabilidades de " + pokemon + ": ")

habilidades = datos["abilities"]
for i, habilidad in enumerate(habilidades, start=1):
    nombre_habilidad = habilidad["ability"]["name"]
    print(f"{i}. {nombre_habilidad}")

print("\nTipos de " + pokemon + ": ")
tipos = datos["types"]
for i, tipo in enumerate(tipos, start=1):
    nombre_tipo = tipo["type"]["name"]
    print(f"{i}. {nombre_tipo}")

#Agregar información al archivo json
archivo = f"pokedex/{pokemon.lower()}.json"
with open(archivo, 'w') as archivo_json:
    datos["image_url"] = url_imagen
    json.dump(datos, archivo_json, indent=4)

print(f"\nLa información de {pokemon} ha sido guardada en '{archivo}'.")
