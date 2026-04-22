import random


#crear la clase de olimpics



class Participant():

    def __init__(self,name, country):
        self.name = name
        self.country = country

    def __eq__(self, other):
        if isinstance(other, Participant):
            return self.name == other.name and self.country == other.country
        return False

    def __hash__(self):
        return hash((self.name, self.country))

    def __str__(self):
        return f'{self.name} del pais {self.country}'






class Olimpics:
    def __init__(self):
        self.events = []
        self.participants = {}
        self.results = {}
        self.country_results = {}

    def register_event(self):

        event = input ('Que evento quieres dar de alta: \n')
        if event not in self.events:
            self.events.append(event)
            print(f'Evento {event} registrado correctamente')
        else:
            print('El evento ya existe')
            return

    def register_participant(self):

        print('------------------Registro de participante')

        if not self.events:
            print('No hay eventos añade al menos un evento')
            return


        name = input('Ingrese el nombre del participante: ')
        country = input('Ingrese el país del participante: ')


        participant = Participant(name,country)
        print(f'Participante {participant} creado')

        print('Eventos disponibles')
        for index, event in enumerate(self.events):
            print(f'{index + 1} - {event} ')

        event_choice =  int(input('Elije un evento: ')) -1

        if  event_choice >= 0 and event_choice < len(self.events):

            event = self.events[event_choice]

            if event in self.participants and participant in self.participants[event]:
                print(f'El participante {name} del pais {country} ya está registrado en el evento {event}')
                return

            else:
                if not self.participants:
                    self.participants[event] = []

                self.participants[event].append(participant)
                print(f'El participante {name} del pais {country} ha sido registrado en el evento {event}')

        else:
            print('Opción de evento no válida')
            return


    def simulate_event(self):

        if not self.events:
            print('No hay eventos añade al menos un evento')
            return
        for event in self.events:

            if len(self.participants[event]) < 3:
                print('Tiene que haber al menos 3 participantes en los eventos.')
            continue

        event_participants = random.sample(self.participants[event], 3) #si hay mas de 3 recoge al azar 3 de ellos
        random.shuffle(event_participants)

        gold, silver , bronze = event_participants
        self.results[event] = [gold, silver, bronze]

        self.update_country_results(gold.country, 'gold')
        self.update_country_results(silver.country, 'silver')
        self.update_country_results(bronze.country, 'bronze')

        print(f'Similacion de evento {event} realizada')
        print(f'Ganador: {gold.name} del pais {gold.country}')
        print(f'2º lugar: {silver.name} del pais {silver.country}')
        print(f'3º lugar: {bronze.name} del pais {bronze.country}')





    def update_country_results(self,country, medal):
        if country not in self.country_results:
            self.country_results[country] = {'oro': 0, 'plata': 0, 'bronce': 0}

        self.country_results[country][medal] += 1



    def show_report(self):

        print('Informe juegos olimpicos')

        if self.results:
            for event, winners in self.results.items():
                print(f'Evento: {event}')
                print(f'Ganador: {winners[0].name} del pais {winners[0].country}')
                print(f'2º lugar: {winners[1].name} del pais {winners[1].country}')
                print(f'3º lugar: {winners[2].name} del pais {winners[2].country}')
        else:
            print('No hay resultados para mostrar')

        if self.country_results:

            for country, medals in sorted(self.country_results.items(), key=lambda x: (
                x[1]['oro'], x[1]['plata'], x[1]['bronce']), reverse=True):
                print(f'Pais: {country} Oro: {medals["oro"]} Plata: {medals["plata"]} Bronce: {medals["bronce"]}')





        else:
            print('No hay resultados por pais registradas')

        #ganadores por evento
        for event , winners in self.results.items():
            print(f'Evento: {event}')
            print(f'Ganador: {winners[0].name} del pais {winners[0].country}')








olimpic2024 = Olimpics()


print('Bienvenido a la aplicacion de olimpiadas')

while True:
    print('''
    * 1. Registro de eventos.
    * 2. Registro de participantes.
    * 3. Simulación de eventos.
    * 4. Creación de informes.
    * 5. Salir del programa.
    ''')

    option = input('Elija una opción: ')

    match option:
        case '1':
            olimpic2024.register_event()
        case '2':
            olimpic2024.register_participant()
        case '3':
            olimpic2024.simulate_event()
        case '4':
            olimpic2024.show_report()
        case '5':
            print('Gracias por usar la aplicación de olimpiadas. ¡Hasta luego!')
            break
        case _:
            print('Opción inválida. Por favor, elija una opción válida.')

