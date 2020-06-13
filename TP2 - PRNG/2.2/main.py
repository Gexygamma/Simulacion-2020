import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

import dist

tamaño_muestra = 100000
nivel_significancia = 0.05

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

def test(gen):
    data = generar_muestra(gen)
    if gen.tipo == dist.TipoDist.Continua:
        stat, _pvalue = st.kstest(data, gen.scipy_name, args=gen.params, N=tamaño_muestra)
        valor_critico = st.ksone.ppf(1-nivel_significancia/2, tamaño_muestra)
        result = stat < valor_critico
    else:
        frec_data = calc_frec_relativa(data)
        frec_esp = [gen.calc_valor_teorico(i) for i in np.arange(min(data), max(data)+1)]
        stat, _pvalue = st.chisquare(frec_data, frec_esp)
        valor_critico = st.chi2.isf(q=nivel_significancia, df=len(frec_data)-1)
        result = stat < valor_critico
    print(result, stat, valor_critico)

if __name__ == "__main__":
    test(dist.Binomial(10, 0.5))
