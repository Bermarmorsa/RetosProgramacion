import random
import pprint
from xml.etree.ElementTree import indent



#crear registtro de paises y participantes
participantes = {
    "ID_01": {
        "nombre": "Ana",
        "evento": "100 metros lisos",
        "pais": 'España'
    },
    "ID_02": {
        "nombre": "Mary",
        "evento": "100 metros lisos",
        "pais": 'USA'
    },
    "ID_03": {
        "nombre": "Boika",
        "evento": "100 metros lisos",
        "pais": 'Nigeria'
    },
    "ID_04": {
        "nombre": "Juan",
        "evento": "Ciclismo",
        "pais": 'España'
    },
    "ID_05": {
        "nombre": "Michale",
        "evento": "Ciclismo",
        "pais": 'USA'
    },
    "ID_06": {
        "nombre": "Vitorio",
        "evento": "Ciclismo",
        "pais": 'Italia'
    },
    "ID_07": {
        "nombre": "Clara",
        "evento": "Badminton",
        "pais": 'España'
    },
    "ID_08": {
        "nombre": "Ronda",
        "evento": "Badminton",
        "pais": 'USA'
    },
    "ID_09": {
        "nombre": "Mina",
        "evento": "Badminton",
        "pais": 'Italia'
    }
}

def resul_medalla ():
    lista_medallas = ['oro','plata','bronce']
    random.shuffle(lista_medallas)
#    print(lista_medallas)
    return lista_medallas



#crear registro de eventos
def lista_eventos (participantes):
    #recoger todos los eventos distintos del dicionario de participantes para crear una lista de eventos posibles
    lista_eventos = []
    for evento in participantes:
        lista_eventos.append(participantes[evento]['evento'])
    lista_eventos = list(set(lista_eventos))
    return lista_eventos

#print(lista_eventos(participantes))




#simulador de eventos
def sim_eventos (lista_eventos , participantes):
    resultados = {}
    #para cada elemento en lista de elementos recogemos el pais y el nombre del participante
    for evento in lista_eventos:
        lista_medallas = resul_medalla()
        lista_puestos = []
        n = 0
        for id, datos in participantes.items():
            if datos['evento'] == evento:
                id_evento = f"{evento}_{n}"
#                print('-----id_evento--------')
#                print(id_evento)
        #añadir a diccionario resultados registro on id = evento , nombre = datos['nombre'], pais = datos['pais'] y puesto = lista_medallas[n]
                resultados[id_evento] = {
                    "evento": evento,
                    "nombre": datos['nombre'],
                    "pais": datos['pais'],
                    "puesto": lista_medallas[n]
                }
#                print('--------entrada en dicionario-------------')
#                print(resultados)
                n += 1
    return resultados

def informe_resultados (diccionario):


    lista_paises = []
    for id, datos in diccionario.items():
        if datos['pais'] not in lista_paises:
            lista_paises.append(datos['pais'])


    for id, datos in diccionario.items():
        print('------------dic salida ------------')
        print(f"evento: {id}")
        print(f" - Evento: {datos['evento']}")
        print(f" - Nombre: {datos['nombre']}")
        print(f" - pais: {datos['pais']}")
        print(f" - puesto: {datos['puesto']}")

    print('---------------medallas por paises------------')
    for pais in lista_paises :
        oro = 0
        plata = 0
        bronce = 0
        for id, datos in diccionario.items():
            if datos['pais'] == pais:
                if datos['puesto'] == 'oro':
                    oro += 1
                if datos['puesto'] == 'plata':
                    plata += 1
                if datos['puesto'] == 'bronce':
                    bronce += 1
        print(f'{pais} tiene {oro} medallas de oro, {plata} medallas de plata y {bronce} medallas de bronce')

    print('-----------------------------------------------')
    print('------------medallas por eventos---------------')
    print('-----------------------------------------------')
    for evento in lista_eventos(participantes) :
        print(f'Evento: {evento}')
        for id, datos in diccionario.items():
            if datos['evento'] == evento:
                print(f'{datos["nombre"]} , {datos["pais"]} , {datos["puesto"]}')

    print('-----------------------------------------------')
    print('------------Ganadores de cada evento-----------')
    print('-----------------------------------------------')
    for evento in lista_eventos(participantes) :
        print(f'Evento: {evento}')
        for id, datos in diccionario.items():
            if datos['puesto'] == 'oro' and datos['evento'] == evento:
                print(f'{datos["nombre"]} , {datos["pais"]}')








salida= sim_eventos(lista_eventos(participantes) , participantes)
informe_resultados(salida)



#informe final de medallas
