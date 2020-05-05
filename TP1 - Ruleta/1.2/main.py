from archivos.simulacion import Simulacion, calcular_frec_relativa
from archivos.ruleta import Color, Paridad
from archivos.estrategias import Martingala, MartingalaInvertida, MartingalaGrande, Labouchere, LabouchereInvertida, Dalembert, DalembertInvertida
from archivos.graficador import graficar_frec, graficar_simulacion
from time import sleep

def frec_relativa():
    """ Calculo de frecuencia relativa de una tirada favorable. """
    iteraciones = 2000
    tirada_favorable = lambda tirada : tirada.color == Color.ROJO

    frec_relativa = calcular_frec_relativa(iteraciones, tirada_favorable)
    graficar_frec(frec_relativa)

def sim_estrategia():
    """ Simulación de rendimiento de estrategias. """
    cantidad_tiradas = 250
    tirada_favorable = lambda tirada : tirada.color == Color.NEGRO

    sim = Simulacion(cantidad_tiradas, tirada_favorable)
    sim.agregar_estrategia(
        LabouchereInvertida([1,2,3])
    )
    sim.ejecutar()
    graficar_simulacion(sim)

def calc_puntaje():
    """ Simula varias estrategias en paralelo y mide su desempeño. """
    cantidad_tiradas = 2000
    iteraciones = 5000
    tirada_favorable = lambda tirada : tirada.color == Color.ROJO

    dict_puntaje = {}
    for i in range(iteraciones):
        sim = Simulacion(cantidad_tiradas, tirada_favorable)
        sim.agregar_estrategia(
            Martingala(1),
            MartingalaGrande(1),
            MartingalaInvertida(1),
            MartingalaInvertida(1, 30),
            Labouchere([1,2,3]),
            LabouchereInvertida([1,2,3]),
            Dalembert(4),
            DalembertInvertida(4),
            DalembertInvertida(4, 4)
        )
        sim.ejecutar()
        for estrategia in sim.estrategias:
            if i == 0:
                dict_puntaje[str(estrategia)] = []
            barrera_absorcion = estrategia.barrera_absorcion[-1]
            rendimiento = estrategia.rendimiento[-1]
            dict_puntaje[str(estrategia)].append(rendimiento / barrera_absorcion)
        if i % (iteraciones / 100) == 0:
            percentage = i/(iteraciones/100)
            print("Cargando... ", percentage, "%")
            if percentage % 10 == 0 and percentage != 0:
                print('...')
                sleep(15) # Esto esta xq sino el ventilador de mi cpu explota. :(
    print("Fin de la simulación...")
    for str_estrategia, lista_puntaje in dict_puntaje.items():
        print("{:>28}: {:9.6f}".format(str_estrategia, sum(lista_puntaje)/len(lista_puntaje)))

if __name__ == '__main__':
    sim_estrategia()
