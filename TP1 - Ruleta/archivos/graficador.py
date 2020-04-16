import matplotlib.pyplot as plt
import numpy as np
from archivos.simulacion import Simulacion, valores_esperados

frecuencia_esperada, promedio_esperado, variancia_esperada, desvio_esperado = valores_esperados()

def graficar(simulacion, iteraciones, numero):
    plt.subplot(2, 2, 1)
    plt.plot(simulacion.frecuencias)
    plt.plot([0, iteraciones-1], [frecuencia_esperada, frecuencia_esperada])
    plt.ylabel('Frec. Rel. para ' + str(numero))
    plt.xlabel('Nro iteración')

    plt.subplot(2, 2, 2)
    plt.plot(simulacion.promedios)
    plt.plot([0, iteraciones-1], [promedio_esperado, promedio_esperado])
    plt.ylabel('Promedio')
    plt.xlabel('Nro iteración')

    plt.subplot(2, 2, 3)
    plt.plot(simulacion.variancias)
    plt.plot([0, iteraciones-1], [variancia_esperada, variancia_esperada])
    plt.ylabel('Variancia')
    plt.xlabel('Nro iteración')

    plt.subplot(2, 2, 4)
    plt.plot(simulacion.desvios)
    plt.plot([0, iteraciones-1], [desvio_esperado, desvio_esperado])
    plt.ylabel('Desvío')
    plt.xlabel('Nro iteración')

    plt.tight_layout()
    plt.show()

def graficar_multiples(simulaciones, iteraciones, numero):
    plt.subplot(2, 2, 1)
    for sim in simulaciones:
        plt.plot(sim.frecuencias)
    plt.plot([0, iteraciones-1], [frecuencia_esperada, frecuencia_esperada])
    plt.ylabel('Frec. Rel. para ' + str(numero))
    plt.xlabel('Nro iteración')

    plt.subplot(2, 2, 2)
    for sim in simulaciones:
        plt.plot(sim.promedios)
    plt.plot([0, iteraciones-1], [promedio_esperado, promedio_esperado])
    plt.ylabel('Promedio')
    plt.xlabel('Nro iteración')

    plt.subplot(2, 2, 3)
    for sim in simulaciones:
        plt.plot(sim.variancias)
    plt.plot([0, iteraciones-1], [variancia_esperada, variancia_esperada])
    plt.ylabel('Variancia')
    plt.xlabel('Nro iteración')

    plt.subplot(2, 2, 4)
    for sim in simulaciones:
        plt.plot(sim.desvios)
    plt.plot([0, iteraciones-1], [desvio_esperado, desvio_esperado])
    plt.ylabel('Desvío')
    plt.xlabel('Nro iteración')
    
    plt.tight_layout()
    plt.show()