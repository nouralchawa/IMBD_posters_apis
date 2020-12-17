import requests

direccion = "http://www.omdbapi.com/?apikey=f36cb021&i=tt3896198"  #url a laque quiero llamar

#Hacer peticion HTTP
respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    print(respuesta.text)
    
    datos = respuesta.json()
    print (datos)
else: 
    print("Se ha popducido un error", respuesta.status_code)

