class Estrategia(object):

    def __init__(self, apuesta_inicial):
        self.apuesta = [apuesta_inicial]
        self.rendimiento = [0]
        self.barrera_absorcion = [apuesta_inicial]
    
    def calcular_rendimiento(self, tirada_favorable):
        return self.rendimiento[-1] + self.apuesta[-1] * (int(tirada_favorable) * 2 - 1)
    
    def calcular_apuesta(self, tirada_favorable):
        raise NotImplementedError('Apuesta de la estrategia no implementada.')

    def calcular_barrera(self, rendimiento, apuesta):
        return max(apuesta - rendimiento, self.barrera_absorcion[-1])
        
    def ejecutar(self, tirada_favorable):
        rendimiento = self.calcular_rendimiento(tirada_favorable)
        apuesta = self.calcular_apuesta(tirada_favorable)
        barrera_absorcion = self.calcular_barrera(rendimiento, apuesta)
        self.rendimiento.append(rendimiento)
        self.apuesta.append(apuesta)
        self.barrera_absorcion.append(barrera_absorcion)

class Martingala(Estrategia):

    LENTO = 0
    RAPIDO = 1

    def __init__(self, apuesta_minima, tipo_estrategia):
        self.apuesta_minima = apuesta_minima
        self.tipo_estrategia = tipo_estrategia
        super().__init__(apuesta_minima)
    
    def __str__(self):
        return "Martingala %s" % ("Rápido" if self.tipo_estrategia else "Lento")

    def calcular_apuesta(self, tirada_favorable):
        return self.apuesta_minima if tirada_favorable else self.apuesta[-1]*2+self.tipo_estrategia
        
class Labouchere(Estrategia):

    def __init__(self, secuencia_inicial):
        self.secuencia_inicial = secuencia_inicial
        self.secuencia_actual = secuencia_inicial.copy()
        super().__init__(self.secuencia_actual[0] + self.secuencia_actual[-1])
    
    def __str__(self):
        return "Labouchere"
    
    def calcular_apuesta(self, tirada_favorable):
        if tirada_favorable:
            if len(self.secuencia_actual) > 2:
                self.secuencia_actual.pop(0)
                self.secuencia_actual.pop()
            else:
                self.secuencia_actual = self.secuencia_inicial.copy()
        else:
            self.secuencia_actual.append(self.apuesta[-1])
        return self.secuencia_actual[0] + self.secuencia_actual[-1]

class Dalembert(Estrategia):

    def __init__(self, secuencia_inicial):
        super().__init__(0)
    
    def __str__(self):
        "D\'alembert"
    
    def calcular_apuesta(self, tirada_favorable):
        raise NotImplementedError('Estrategia no implementada.')
