from archivos.ruleta import Tirada

def calcular_frec_relativa(iteraciones, tirada_favorable):
    """ Calcula la frecuencia relativa de obtener una tirada favorable. """
    frec_relativa = []
    for cantidad_tiradas in range(1, iteraciones+1):
        frec_absoluta = 0
        for _i in range(cantidad_tiradas):
            if tirada_favorable(Tirada()):
                frec_absoluta += 1
        frec_relativa.append(frec_absoluta / cantidad_tiradas)
    return frec_relativa

class Simulacion(object):

    def __init__(self, cantidad_tiradas, tirada_favorable):
        self.estrategias = []
        self.cantidad_tiradas = cantidad_tiradas
        self.tirada_favorable = tirada_favorable
    
    def agregar_estrategia(self, *args):
        """ Agrega una estrategia de apuesta a la simulación. """
        for estrategia in args:
            self.estrategias.append(estrategia)
    
    def ejecutar(self):
        """ Corre la simulación. Ejecuta todos los algoritmos cargados. """
        for _i in range(self.cantidad_tiradas):
            tirada = Tirada()
            for estrategia in self.estrategias:
                estrategia.ejecutar(self.tirada_favorable(tirada))
