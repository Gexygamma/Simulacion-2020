import matplotlib.pyplot as plt
from archivos.simulacion import Simulacion

def graficar(simulacion):
    plt.subplot(2, 2, 1)
    plt.plot(simulacion.frecuencias)

    plt.subplot(2, 2, 2)
    plt.plot(simulacion.promedios)

    plt.subplot(2, 2, 3)
    plt.plot(simulacion.variancias)

    plt.subplot(2, 2, 4)
    plt.plot(simulacion.desvios)

    plt.show()

def graficar_multiples(simulaciones):
    plt.subplot(2, 2, 1)
    for sim in simulaciones:
        plt.plot(sim.frecuencias)

    plt.subplot(2, 2, 2)
    for sim in simulaciones:
        plt.plot(sim.promedios)

    plt.subplot(2, 2, 3)
    for sim in simulaciones:
        plt.plot(sim.variancias)

    plt.subplot(2, 2, 4)
    for sim in simulaciones:
        plt.plot(sim.desvios)
    
    plt.show()