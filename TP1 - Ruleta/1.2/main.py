from archivos.simulacion import Simulacion, calcular_frec_relativa
from archivos.ruleta import Color
from archivos.estrategias import Martingala, Labouchere, Dalembert
from archivos.graficador import graficar_frec, graficar_simulacion

def frec_relativa():
    """ Calculo de frecuencia relativa de una tirada favorable. """
    iteraciones = 2000
    tirada_favorable = lambda tirada : tirada.color == Color.ROJO

    frec_relativa = calcular_frec_relativa(iteraciones, tirada_favorable)
    graficar_frec(frec_relativa)

def sim_estrategia():
    """ Simulación de rendimiento de estrategias. """
    cantidad_tiradas = 100
    tirada_favorable = lambda tirada : tirada.color == Color.ROJO

    sim = Simulacion(cantidad_tiradas, tirada_favorable)
    sim.agregar_estrategia(
        Martingala(1, Martingala.LENTO),
        Martingala(1, Martingala.RAPIDO)
    )
    sim.ejecutar()
    graficar_simulacion(sim)

if __name__ == '__main__':
    sim_estrategia()
