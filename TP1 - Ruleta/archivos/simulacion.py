import numpy as np

TAMAÑO_RULETA = 36
INCLUIR_CERO = True

def valores_esperados():
    ruleta = np.arange(not INCLUIR_CERO, TAMAÑO_RULETA+1)

    frecuencia_esperada = 1/len(ruleta)
    promedio_esperado = np.average(ruleta)
    variancia_esperada = np.var(ruleta)
    desvio_esperado = np.std(ruleta)
    
    return frecuencia_esperada, promedio_esperado, variancia_esperada, desvio_esperado

class Simulacion(object):
    def __init__(self):
        self.frecuencias = []
        self.promedios = []
        self.desvios = []
        self.variancias = []
    
    def generar_iteracion(self, cantidad_tiradas):
        return np.random.randint(not INCLUIR_CERO, TAMAÑO_RULETA+1, size=cantidad_tiradas)

    def ejecutar(self, iteraciones, numero):
        for cantidad_tiradas in range(1, iteraciones+1):
            iteracion = self.generar_iteracion(cantidad_tiradas)
            self.promedios.append(np.average(iteracion))
            self.desvios.append(np.std(iteracion))
            self.variancias.append(np.var(iteracion))

            frec_relativa = 0
            for tirada in iteracion:
                if tirada == numero:
                    frec_relativa += 1
            self.frecuencias.append(frec_relativa/cantidad_tiradas)