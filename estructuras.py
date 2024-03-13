
#se declaran diccionarios = objetos
clienteUno= {
    "id":5,
    "nombre":"edifi1",
    "consumo":200
}
clienteDos= {
    "id":58,
    "nombre":"edifi2",
    "consumo":500
}

#se declara una lista

clientesAsociados=[
    clienteUno,clienteDos
]


#que hago con esa lista?
#mi objetivo sera  obtener la informacion de la lista
#recorrer la lista o arreglo

""" print(clientesAsociados) """

""" for  i in range(2):
    print(clientesAsociados[i]["consumo"]) """

#programemos un foreach que es un for especializado en recorrer arreglos
for cliente in clientesAsociados:
    print(f'{cliente["id"]} => {cliente["consumo"]} KWH')