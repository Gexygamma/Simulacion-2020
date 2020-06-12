import matplotlib.pyplot as plt
import numpy as np

import dist

tamaño_muestra = 100000

def generar_muestra(gen):
    return [gen.generar() for _i in range(tamaño_muestra)]

def calc_frec_relativa(data):
    return [value/len(data) for value in np.bincount(data)[min(data):]]

def mostrar(gen):
    data = generar_muestra(gen)
    if gen.tipo == dist.TipoDist.Continua: # Continua
        # Graficar muestra.
        plt.hist(data, bins='auto', density=True, color='orange')
        # Graficar valor teórico.
        rango = np.linspace(min(data), max(data))
        frec_esp = [gen.calc_valor_teorico(i) for i in rango]
        plt.plot(rango, frec_esp, '--')
    else: # Discreta
        # Graficar muestra.
        frec_data = calc_frec_relativa(data)
        labels = np.arange(min(data), max(data)+1)
        plt.bar(labels, frec_data, tick_label=labels, color='orange')
        # Graficar valor teórico.
        rango = np.arange(min(data), max(data)+1)
        frec_esp = [gen.calc_valor_teorico(i) for i in rango]
        plt.stem(rango, frec_esp, '--', use_line_collection=True)
    plt.show()

if __name__ == "__main__":
    mostrar(dist.Binomial(10, 0.5))
