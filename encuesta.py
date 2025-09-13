# Angie Mesa
# Encuesta 10 personas
 
class Encuesta:
    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.respuestas = []

    def agregar_respuesta(self, nombre, idea, equipo):
        datos = (nombre, idea, equipo)
        self.respuestas.append(datos)

    def mostrar_resultados(self):
        print("\n Resultados de la encuesta ")
        participante = 1
        for estudiante in self.respuestas:
            print("\nParticipante", participante)
            print(self.preguntas[0], estudiante[0])
            print(self.preguntas[1], estudiante[1])
            print(self.preguntas[2], estudiante[2])
            participante += 1


def main():
    preguntas = (
        "Como te llamas?",
        "Cual es tu idea de proyecto?",
        "Te gusta trabajar en equipo?"
    )

    encuesta = Encuesta(preguntas)

    print(" Encuesta para 10 personas")
    for i in range(10):
        print(f"\n Persona {i+1} ---")
        nombre = input(preguntas[0] + " ")
        idea = input(preguntas[1] + " ")
        equipo = input(preguntas[2] + " ")

        encuesta.agregar_respuesta(nombre, idea, equipo)

    encuesta.mostrar_resultados()

if __name__ == "__main__":
    main()