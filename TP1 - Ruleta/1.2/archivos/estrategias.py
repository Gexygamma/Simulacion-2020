class Estrategia(object):

    def __init__(self, apuesta_inicial):
        self.apuesta = [apuesta_inicial]
        self.rendimiento = [0]
        self.barrera_absorcion = [apuesta_inicial]
    
    def ejecutar(self, tirada_favorable):
        """ Simula la ejecución de una sola tirada, siguiendo un algoritmo específico. """
        raise NotImplementedError('Ejecución de la estrategia no implementada.')

    def guardar_variables(self, rendimiento, apuesta):
        """ Guarda variables para el posterior gráfico """
        self.rendimiento.append(rendimiento)
        self.apuesta.append(apuesta)
        if apuesta - rendimiento > self.barrera_absorcion[-1]:
            self.barrera_absorcion.append(apuesta - rendimiento)
        else:
            self.barrera_absorcion.append(self.barrera_absorcion[-1])

class Martingala(Estrategia):

    LENTO = 0
    RAPIDO = 1

    def __init__(self, apuesta_minima, tipo_estrategia):
        self.apuesta_minima = apuesta_minima
        self.tipo_estrategia = tipo_estrategia
        super().__init__(apuesta_minima)
    
    def __str__(self):
        return "Martingala %s" % ("Rápido" if self.tipo_estrategia else "Lento")

    def ejecutar(self, tirada_favorable):
        if tirada_favorable:
            rendimiento = self.rendimiento[-1]+self.apuesta[-1]
            apuesta = self.apuesta_minima
        else:
            rendimiento = self.rendimiento[-1]-self.apuesta[-1]
            apuesta = self.apuesta[-1]*2+self.tipo_estrategia
        super().guardar_variables(rendimiento, apuesta)
        
class Labouchere(Estrategia):

    def __init__(self, secuencia_inicial):
        self.secuencia_inicial = secuencia_inicial
        self.apuesta_actual = secuencia_inicial[0] + secuencia_inicial[-1]
        super().__init__(self.apuesta_actual)
    
    def __str__(self):
        return "Labouchere"
    
    def ejecutar(self, tirada_favorable):
        raise NotImplementedError('Estrategia no implementada.')

class Dalembert(Estrategia):

    def __init__(self, secuencia_inicial):
        super().__init__(0)
    
    def __str__(self):
        "D\'alembert"
    
    def ejecutar(self, tirada_favorable):
        raise NotImplementedError('Estrategia no implementada.')
