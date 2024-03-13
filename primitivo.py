idClienteUno="afc001"
nombreClienteUno= "Edificio las Manzanas"
cantidadPanelesInstalados= 5
consumoEnergeticoDiario=200
ubicacionClienteUno="clle 10 #43-20"

# se declaron diccionarios (son objetos)
clienteUno={
    "id": 5,
    "nombre": "edificio1",
    "consumo": 200
}

clienteDos={
    "id": 12,
    "nombre": "edificio2",
    "consumo": 500
}

#se declara una lista (es un arreglo)

clientesAsociados=[
    clienteUno, clienteDos
]


#y hora que hago con esto 
# mi objetivo sera recorrer la informacion de la lista

""" print(clientesAsosiados) """
""" for i in  range(2):
    print(clientesAsosiados[i])
    print(clientesAsosiados[i]["consumo"]) """

# programemos un foreach que es un for 
#especualizado en recorrer arreglos 

for cliente in clientesAsociados:
  print(cliente["consumo"]) 
  print(f'{cliente["id"]} => {cliente["consumo"]} KWH')
  print(f'{cliente["id"]} => {cliente["consumo"]} KWH')


