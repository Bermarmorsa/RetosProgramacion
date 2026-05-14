import random

class Sombrero:
    def __init__(self):
        self.casas = {
            "Frontend": 0,
            "Backend": 0,
            "Mobile": 0,
            "Data": 0
        }
        self.preguntas = [
            {"pregunta": "¿Te gusta trabajar con HTML y CSS?", "opciones": ["Sí", "No"], "casas": {"Frontend": 5, "Backend": -2, "Mobile": -1, "Data": -1}},
            {"pregunta": "¿Te gustan las bases de datos?", "opciones": ["Sí", "No"], "casas": {"Frontend": -1, "Backend": 3, "Mobile": -1, "Data": 5}},
            {"pregunta": "¿Te gusta trabajar con frameworks como React o Angular?", "opciones": ["Sí", "No"], "casas": {"Frontend": 4, "Backend": -2, "Mobile": -1, "Data": -1}},
            {"pregunta": "¿Te gustan las redes sociales y la programación de aplicaciones móviles?", "opciones": ["Sí", "No"], "casas": {"Frontend": -1, "Backend": -1, "Mobile": 4, "Data": -1}},
            {"pregunta": "¿Te gusta la programación funcional y trabajar con lenguajes como Haskell o Lisp?", "opciones": ["Sí", "No"], "casas": {"Frontend": -2, "Backend": 3, "Mobile": -1, "Data": -1}},
            {"pregunta": "¿Te gustan los algoritmos de búsqueda y ordenamiento?", "opciones": ["Sí", "No"], "casas": {"Frontend": -1, "Backend": 2, "Mobile": -1, "Data": 4}},
            {"pregunta": "¿Te gusta la programación orientada a objetos?", "opciones": ["Sí", "No"], "casas": {"Frontend": 3, "Backend": 5, "Mobile": -1, "Data": -1}},
            {"pregunta": "¿Te gustan los sistemas de gestión de bases de datos?", "opciones": ["Sí", "No"], "casas": {"Frontend": -2, "Backend": 4, "Mobile": -1, "Data": 3}},
            {"pregunta": "¿Te gusta la programación paralela y el procesamiento de datos en gran escala?", "opciones": ["Sí", "No"], "casas": {"Frontend": -1, "Backend": -2, "Mobile": -1, "Data": 5}},
            {"pregunta": "¿Te gustan las redes de computadoras y la programación de sistemas operativos?", "opciones": ["Sí", "No"], "casas": {"Frontend": -3, "Backend": 4, "Mobile": -2, "Data": -1}},
        ]

    def ejecutar(self):
        nombre = input("¿Cuál es tu nombre? ")
        for i in range(len(self.preguntas)):
            print(f"Pregunta {i+1}: {self.preguntas[i]['pregunta']}")
            respuesta = input("Respuesta: ")
            if respuesta == self.preguntas[i]["opciones"][0]:
                self.casas[self.preguntas[i]["casas"].keys()[0]] += self.preguntas[i]["casas"][self.preguntas[i]["casas"].keys()[0]]
            elif respuesta == self.preguntas[i]["opciones"][1]:
                self.casas[self.preguntas[i]["casas"].keys()[1]] += self.preguntas[i]["casas"][self.preguntas[i]["casas"].keys()[1]]

        max_casa = None
        for casa, puntos in self.casas.items():
            if max_casa is None or puntos > self.casas[max_casa]:
                max_casa = casa

        print(f"¡El sombrero ha decidido que perteneces a la casa {max_casa}!")

        if list(self.casas.values()).count(max(self.casas.values())) == 2:
            sorted_casas = sorted(self.casas.items(), key=lambda x: x[1], reverse=True)
            if sorted_casas[0][1] == sorted_casas[1][1]:
                print("La decisión ha sido complicada. ¡Tienes una ligera ventaja en la casa {sorted_casas[0][0]}!")
            else:
                print(f"¡Tienes una clara ventaja en la casa {sorted_casas[0][0]}!")

if __name__ == "__main__":
    sombrero = Sombrero()
    sombrero.ejecutar()
