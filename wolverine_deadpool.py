import random
import time


'''
/*
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
 */
'''

class Wolverine:

    def __init__(self,vida = 300,regeneracion = 5):
        self.vida = vida
        self.regeneracion = regeneracion

    def __str__(self):
        return f'Lobezno tiene {str(self.vida)} de vida y {str(self.regeneracion)} de regeneracion'

    def danho(self):
        return random.randint(10,120)

    def evitar_ataque(self):
        if random.randint(1, 4) == 1:
            return True
        else:
            return False



class Deadpool:

    def __init__(self,vida = 300,regeneracion = 5):
        self.vida = vida
        self.regeneracion = regeneracion

    def __str__(self):
        return f'Deadpool tiene {self.vida} de vida y {self.regeneracion} de regeneracion'


    def danho(self):
        return random.randint(10,100)

    def evitar_ataque(self):

        if random.randint(1,5) == 1:
            return True
        else:
            return False







class Batalla:

    def __init__(self,turno = 1):
        self.turno = turno




    def sorteo(self):
        lista_oponentes = ['Lobezno','Deadpool']
        random.shuffle(lista_oponentes)
        print(f'Inicia: {lista_oponentes[0]}')
        return lista_oponentes[0]

    def inicio_lucha(self,inicia):
        #iniciamos los personajes
        lobezno = Wolverine()
        print('\n')
        print(lobezno)
        deadpool = Deadpool()
        print(deadpool)
        print('\n')

        while lobezno.vida > 0 and deadpool.vida > 0:
            time.sleep(5)
            if inicia == 'Lobezno':
                l_danho = lobezno.danho()
                if deadpool.evitar_ataque():
                    print(f'Turno {self.turno}: Lobezno ataca con {l_danho} de daño')
                    print(f'Deadpool ha evitado el ataque y queda con {deadpool.vida} de vida\n')
                    print('-'*40)
                    self.turno += 1
                    inicia = 'Deadpool'

                elif not deadpool.evitar_ataque() and l_danho > 70:
                    deadpool.vida -= l_danho
                    print(f'Turno {self.turno}: Lobezno ataca con {l_danho} de daño')
                    print(f'Deadpool ha sufrido el ataque y queda con {deadpool.vida} de vida\n')
                    print(f'Como ha sufrido el daño máximo no podrá atacar el proximo turno \n')
                    deadpool.vida += deadpool.regeneracion
                    print(f'Pero por el descaso recupera {deadpool.regeneracion} de vida y queda en {deadpool.vida} de vida \n')
                    print('-'*40)
                    self.turno += 1
                    inicia = 'Lobezno'

                else:
                    deadpool.vida -= l_danho
                    print(f'Turno {self.turno}: Lobezno ataca con {l_danho} de daño')
                    print(f'Deadpool ha sufrido el ataque y queda con {deadpool.vida} de vida\n')
                    print('-'*40)
                    self.turno += 1
                    inicia = 'Deadpool'

            else:
                d_danho = deadpool.danho()
                if lobezno.evitar_ataque():
                    print(f'Turno: {self.turno}: Deadpool ataca con {d_danho} de daño')
                    print(f'Lobezno ha evitado el ataque y queda con {lobezno.vida} de vida \n')
                    print('-'*40)
                    self.turno += 1
                    inicia = 'Lobezno'


                elif not lobezno.evitar_ataque() and d_danho > 70:
                    lobezno.vida -= d_danho
                    print(f'Turno {self.turno}: Deadpool ataca con {d_danho} de daño')
                    print(f'Lobezno ha sufrido el ataque y queda con {lobezno.vida} de vida\n')
                    print(f'Como ha sufrido el daño máximo no podrá atacar el proximo turno \n')
                    lobezno.vida += lobezno.regeneracion
                    print(f'Pero por el descaso recupera {lobezno.regeneracion} de vida y queda en {lobezno.vida} de vida \n')
                    print('-'*40)
                    self.turno += 1
                    inicia = 'Deadpool'


                else:
                    lobezno.vida -= d_danho
                    print(f'Turno: {self.turno}: Deadpool ataca con {d_danho} de daño')
                    print(f'Lobezno ha sufrido el ataque y queda con {lobezno.vida} de vida\n')
                    print('-'*40)
                    self.turno += 1
                    inicia = 'Lobezno'


        if lobezno.vida <= 0:
            print('Lobezno ha ganado')
            print('\n')
            print('\n')
        else:
            print('Deadpool ha ganado')
            print('\n')
            print('\n')




batalla = Batalla()

while True:
    resultado = ''
    print('Bienvenidos a la batalla entre Wolverine y Deadpool')
    print('-----------------------------------------------------\n \n')
    print('Primero se sorteará quien inicia la batalla Lobezno o Deadpool')
    inicio_sorteo = input('Para iniciar el sorteo pulse s: ')
    if inicio_sorteo == 's':
        resultado = batalla.sorteo()
    else:
        print('Presione la tecla s')
    inicio_batalla = input('Para iniciar la batalla pulse s:')
    if inicio_batalla == 's':
        batalla.inicio_lucha(resultado)






