import matplotlib.pyplot as plt
import numpy as np

import dist

tamaño_muestra = 100000

def generar_muestra(dist, **kwargs):
    return [dist(**kwargs) for _i in range(tamaño_muestra)]

def mostrar_continua(dist, **kwargs):
    data = generar_muestra(dist, **kwargs)
    plt.hist(data, bins=50, density=True)
    plt.show()

def mostrar_discreta(dist, **kwargs):
    data = generar_muestra(dist, **kwargs)
    bar_data = [value/len(data) for value in np.bincount(data)[min(data):]]
    labels = np.arange(min(data), max(data)+1)
    plt.bar(labels, bar_data, tick_label=labels)
    plt.show()

if __name__ == "__main__":
    # mostrar_xxx(distribucion, argumentos)
    mostrar_discreta(dist.binomial, n=10, p=0.5)
