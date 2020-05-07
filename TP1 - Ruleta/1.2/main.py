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
        Martingala(1),
        MartingalaGrande(1),
        Labouchere([1,2,3,4]),
        Dalembert(4)
    )
    sim.ejecutar()
    graficar_simulacion(sim)

if __name__ == '__main__':
    sim_estrategia()
