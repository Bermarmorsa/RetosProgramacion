import random
import time



class Wolverine:

    def __init__(self,vida = 300,regeneracion = 40):
        self.vida = vida
        self.regeneracion = regeneracion

    def __str__(self):
        return f'Lobezno tiene {str(self.vida)} de vida y {str(self.regeneracion)} de regeneracion'

    def danho(self):
        return random.randint(10,100)

    def evitar_ataque(self):
        if random.randint(1, 4) == 1:
            return True
        else:
            return False



class Deadpool:

    def __init__(self,vida = 324,regeneracion = 29):
        self.vida = vida
        self.regeneracion = regeneracion

    def __str__(self):
        return f'Deadpool tiene {self.vida} de vida y {self.regeneracion} de regeneracion'


    def danho(self):
        return random.randint(10,100)

    def evitar_ataque(self):

        if random.randint(1,4) == 1:
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
            time.sleep(0.00000000000000000000001)
            if inicia == 'Lobezno':
                l_danho = lobezno.danho()
                le_ataque = deadpool.evitar_ataque()
                if le_ataque:
                    print(f'Turno {self.turno}: Lobezno ataca con {l_danho} de daño')
                    print(f'Deadpool ha evitado el ataque y queda con {deadpool.vida} de vida\n')
                    print('-'*40)
                    self.turno += 1
                    inicia = 'Deadpool'

                elif not le_ataque and l_danho > 70:
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
                e_ataque = lobezno.evitar_ataque()
                if e_ataque:
                    print(f'Turno: {self.turno}: Deadpool ataca con {d_danho} de daño')
                    print(f'Lobezno ha evitado el ataque y queda con {lobezno.vida} de vida \n')
                    print('-'*40)
                    self.turno += 1
                    inicia = 'Lobezno'


                elif not e_ataque and d_danho > 70:
                    lobezno.vida -= d_danho
                    print(f'Turno {self.turno}: Deadpool ataca con {d_danho} de daño')
                    print(f'Lobezno ha sufrido el ataque y queda con {lobezno.vida} de vida\n')
                    print(f'Como ha sufrido el daño máximo no podrá atacar el proximo turno\n')
                    lobezno.vida += lobezno.regeneracion
                    print(f'Pero por el descaso recupera {lobezno.regeneracion} de vida y queda en {lobezno.vida} de vida\n')
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
            print('Deadpool ha ganado')
            print('\n')
            print('\n')
            return 'd'
        else:
            print('Lobezno ha ganado')
            print('\n')
            print('\n')
            return 'l'




batalla = Batalla()

lobezno_wins = 0
deadpool_wins = 0
max_com = 10000

for item in range(0,10000):
    print('Bienvenidos a la batalla entre Wolverine y Deadpool')
    print('-----------------------------------------------------\n \n')
    print('Primero se sorteará quien inicia la batalla Lobezno o Deadpool')
    resultado = batalla.sorteo()
    wins = batalla.inicio_lucha(resultado)
    if wins == 'l':
        lobezno_wins += 1
    elif wins == 'd':
        deadpool_wins += 1
    else:
        print(f'Error {wins}')

print(f'Lobezno ha ganado {lobezno_wins} combates, un {round(lobezno_wins/max_com*100,2)}% de victorias')
print(f'Deadpool ha ganado {deadpool_wins} combates, un {round(deadpool_wins/max_com*100,2)}% de victorias')
