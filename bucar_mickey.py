





'''
* EJERCICIO:
 * ¡Disney ha presentado un montón de novedades en su D23!
 * Pero... ¿Dónde está Mickey?
 * Mickey Mouse ha quedado atrapado en un laberinto mágico
 * creado por Maléfica.
 * Desarrolla un programa para ayudarlo a escapar.
 * Requisitos:
 * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
 * 2. Los valores de las celdas serán:
 *    - ⬜️ Vacío
 *    - ⬛️ Obstáculo
 *    - 🐭 Mickey
 *    - 🚪 Salida
 * Acciones:
 * 1. Crea una matriz que represente el laberinto (no hace falta
 * que se genere de manera automática).
 * 2. Interactúa con el usuario por consola para preguntarle hacia
 * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 * 3. Muestra la actualización del laberinto tras cada desplazamiento.
 * 4. Valida todos los movimientos, teniendo en cuenta los límites
 * del laberinto y los obstáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
'''

class Laberinto():

    def __init__(self):
        self.matriz = [  ["🐭","⬜️","⬛️","⬜️","⬜️","⬜️"],
                         ["⬜️","⬛️","⬜️","⬜️","⬛️","⬜️"],
                         ["⬜️","⬜️","⬜️","⬛️","⬜️","⬜️"],
                         ["⬛️","⬛️","⬜️","⬜️","⬜️","⬛️"],
                         ["⬜️","⬜️","⬛️","⬜️","⬛️","⬜️"],
                         ["⬜️","⬜️","⬜️","⬜️","⬜️","🚪"]]

        self.mickey = [0,0]
        self.salida = True


    def show_laberinth(self):

        for row in self.matriz:
            print("".join(row))
        print()


    def movimiento(self):
        chioce = input('Puedes moverte con las flechas. A donde quieres ir: w(arriba),s(abajo),a(izquierda),d(derecha) ')

        curr_x , curr_y = self.mickey

        new_x, new_y = curr_x , curr_y


        match chioce:
            case 'w':
                new_x = curr_x - 1
            case 's':
                new_x = curr_x + 1
            case 'a':
                new_y = curr_y - 1
            case 'd':
                new_y = curr_y + 1
            case _:
                print('Dirrecion erronera\n')

        if new_x < 0 or new_x > 5 or new_y < 0 or new_y > 5:
            print('Te sales del tablero\n')


        else:

            if self.matriz[new_x][new_y] == "⬛️":
                print('Hay un obstáculo no puedes pasar')


            elif self.matriz[new_x][new_y] == "🚪":
                self.matriz[curr_x][curr_y] = "⬜️"
                self.matriz[new_x][new_y] = "🐭"
                print('Has llegado a la salida')
                self.salida = False



            else:
                self.matriz[curr_x][curr_y] = "⬜️"
                self.matriz[new_x][new_y] = "🐭"
                self.mickey = [new_x,new_y]














laberinto = Laberinto()




while laberinto.salida:
    laberinto.show_laberinth()
    laberinto.movimiento()






