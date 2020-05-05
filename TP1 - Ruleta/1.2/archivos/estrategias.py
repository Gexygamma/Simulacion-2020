from enum import Enum, auto
import math

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

    def __init__(self, apuesta_minima):
        self.apuesta_minima = apuesta_minima
        super().__init__(apuesta_minima)
    
    def __str__(self):
        return "Martingala Simple"

    def calcular_apuesta(self, tirada_favorable):
        return self.apuesta_minima if tirada_favorable else self.apuesta[-1]*2

class MartingalaGrande(Martingala):

    def __init__(self, apuesta_minima):
        super().__init__(apuesta_minima)
    
    def __str__(self):
        return "Martingala Grande"

    def calcular_apuesta(self, tirada_favorable):
        apuesta = super().calcular_apuesta(tirada_favorable)
        return apuesta if tirada_favorable else apuesta+1

class MartingalaInvertida(Martingala):

    def __init__(self, apuesta_minima, limite=None):
        if limite == None:
            self.limite = 0
        else:
            self.limite = limite
        super().__init__(apuesta_minima)

    def __str__(self):
        return "Martingala Inv. " + ("con L=%d" % self.limite if self.limite > 0 else "Ilimitada")
    
    def calcular_apuesta(self, tirada_favorable):
        if tirada_favorable:
            apuesta = self.apuesta[-1]*2
            if self.limite != 0 and math.floor(apuesta) > self.limite:
                return self.apuesta_minima
            else:
                return apuesta
        else:
            return self.apuesta_minima
        
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

class LabouchereInvertida(Labouchere):

    def __init__(self, secuencia_inicial):
        super().__init__(secuencia_inicial)
    
    def __str__(self):
        return "Labouchere Inv."
    
    def calcular_apuesta(self, tirada_favorable):
        return super().calcular_apuesta(not tirada_favorable)

class Dalembert(Estrategia):

    def __init__(self, apuesta_base):
        self.apuesta_base = apuesta_base
        super().__init__(apuesta_base)
    
    def __str__(self):
        return "D\'Alembert Normal"
    
    def calcular_apuesta(self, tirada_favorable):
        if tirada_favorable:
            return max(self.apuesta[-1] - self.apuesta_base, self.apuesta_base)
        else:
            return self.apuesta[-1] + self.apuesta_base

class DalembertInvertida(Dalembert):

    def __init__(self, apuesta_base, limite_unidades=None):
        if limite_unidades is None:
            self.limite_unidades = 0
        else:
            self.limite_unidades = limite_unidades
        super().__init__(apuesta_base)

    def __str__(self):
        return "D\'Alembert Inv. " + ("con L=%du" % self.limite_unidades if self.limite_unidades > 0 else "Ilimitada")
    
    def calcular_apuesta(self, tirada_favorable):
        if tirada_favorable:
            apuesta = self.apuesta[-1] + self.apuesta_base
            if self.limite_unidades != 0 and math.floor(apuesta) > self.limite_unidades * self.apuesta_base:
                return self.apuesta_base
            else:
                return apuesta
        else:
            return max(self.apuesta[-1] - self.apuesta_base, self.apuesta_base)
