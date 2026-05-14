'''
/*
 * EJERCICIO:
 * Cada año se celebra el Batman Day durante la tercera semana de septiembre...
 * ¡Y este año cumple 85 años! Te propongo un reto doble:
 *
 * RETO 1:
 * Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta
 * su 100 aniversario.
 *
 * RETO 2:
 * Crea un programa que implemente el sistema de seguridad de la Batcueva.
 * Este sistema está diseñado para monitorear múltiples sensores distribuidos
 * por Gotham, detectar intrusos y activar respuestas automatizadas.
 * Cada sensor reporta su estado en tiempo real, y Batman necesita un programa
 * que procese estos datos para tomar decisiones estratégicas.
 * Requisitos:
 * - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
 * - Cada sensor se identifica con una coordenada (x, y) y un nivel
 *   de amenaza entre 0 a 10 (número entero).
 * - Batman debe concentrar recursos en el área más crítica de Gotham.
 * - El programa recibe un listado de tuplas representando coordenadas de los
 *   sensores y su nivel de amenaza. El umbral de activación del protocolo de
 *   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
 * Acciones:
 * - Identifica el área con mayor concentración de amenazas
 *   (sumatorio de amenazas en una cuadrícula 3x3).
 * - Si el sumatorio de amenazas es mayor al umbral, activa el
 *   protocolo de seguridad.
 * - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
 *   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
 * - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
 *   sus amenazas, la distancia a la Batcueva y si se debe activar el
 *   protocolo de seguridad.
 */

'''
import calendar
from datetime import datetime
import random


fecha_texto = "2026-09-01"
y_init=2026
for i in range(25):


    y_str = str(y_init)
    fecha_texto = f"{y_str}-09-01"

    # %Y = Año (2026), %m = Mes (09), %d = Día (01)
    fecha = datetime.strptime(fecha_texto, "%Y-%m-%d")

    #print(type(fecha)) # Verás que es <class 'datetime.datetime'>
    #print(fecha)

    cal = calendar.monthcalendar(fecha.year, fecha.month)
    print(f'El sabado de la tercera semana de septiembre de {y_str} es el dia {cal[2][5]} ese día es el aniversario Batman')

    y_init = y_init + 1
    i =+ 1




# Generamos 10 filas, cada una con 20 valores aleatorios
matriz = [[random.randint(0, 5) for _ in range(20)] for _ in range(20)]

# Para visualizarla de forma ordenada:

print(matriz[1][1])
print(matriz[18][18])

dicionario_amenazas = {}

for fila in matriz:
    print(fila)


#hacer un bucle que recorra todos los datos de filas y colmunas en orden y devuelva las coordenadas tipo  matriz[1][1]

inicio_diccionario = 0

for x in range(1,19):
    for y in range(1,19):
        sumacradro = matriz[x-1][y-1]+matriz[x-1][y]+matriz[x-1][y+1]+matriz[x][y-1]+matriz[x][y]+matriz[x][y+1]+matriz[x+1][y-1]+matriz[x+1][y]+matriz[x+1][y+1]
        if sumacradro >= 30:
            print(f'Hay una riesgo en las coordenadas de la matriz con x={x} y y={y} y suma({sumacradro})')
            distancia_batcueva = x + y
            dicionario_amenazas[inicio_diccionario] = {'coord_x':x,'coord_y':y,'distancia_batcueva':distancia_batcueva,'amenaza':sumacradro}
            inicio_diccionario += 1


for item, datos in dicionario_amenazas.items():
    print(datos)

if dicionario_amenazas:
    # Encontrar el item con la menor distancia_batcueva
    item_menor_distancia = min(dicionario_amenazas.values(), key=lambda x: x['distancia_batcueva'])

    print(f"\nEl área con menor distancia a la Batcueva es:")
    print(item_menor_distancia)
else:
    print("\nNo se detectaron amenazas que superen el umbral.")