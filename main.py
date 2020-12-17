import requests

API_KEY="f36cb021"
url_busqueda = "http://www.omdbapi.com/?apikey={}&s={}"
url_identificador = "http://www.omdbapi.com/?apikey={}&i={}"

def peticion(url):
    respuesta = requests.get(direccion)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos['Response'] == "False":
            print(datos["Error"])
        else:
            return datos
    else:
        print("Error en consulta:", nueva_respuesta.status_code)


pregunta= input("Titulo de la película: ")

respuesta = peticion(url_busqueda.format(APY_KEY, pregunta))
primera_peli = respuesta['Search'][0]
clave = primera_peli['imdbID']

respuesta = peticion(url_identificador.format(APY_KEY, clave))
titulo = respuesta['Title']
agno = respuesta['Year']
director = respuesta['Director']
print("La película {}, estrenadada en el año {}, fue dirigida por {}".format(titulo, agno, director))



if respuesta.status_code == 200:
    datos = respuesta.json()
    if datos['Response'] == "False":
        print(datos["Error"])
    else:
        primera_peli = datos['Search'][0]
        clave = primera_peli['imdbID']

        otra_direccion = f"http://www.omdbapi.com/?apikey={API_KEY}&i={clave}"
        nueva_respuesta = requests.get(otra_direccion)
        if nueva_respuesta.status_code == 200:
            datos = nueva_respuesta.json()
            if datos['Response'] == "False":
                print(datos["Error"])
            else:
                titulo = datos['Title']
                agno = datos['Year']
                director = datos['Director']
                print("La película {}, estrenadada en el año {}, fue dirigida por {}".format(titulo, agno, director))
        else:
            print("Error en consulta:", nueva_respuesta.status_code)
else:
    print("Error en busqueda:", respuesta.status_code)
