from enum import Enum, auto
import random as rnd
import math

rnd.seed()
numeros_rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

class Color(Enum):
    VERDE = auto()
    NEGRO = auto()
    ROJO = auto()

class Paridad(Enum):
    CERO = auto()
    PAR = auto()
    IMPAR = auto()

class Tirada(object):
    """ Representa un número obtenido de una tirada de ruleta, generado aleatoriamente. """

    def __init__(self):
        self.numero = rnd.randint(0, 36)
    
    @property
    def color(self):
        if self.numero == 0:
            return Color.VERDE
        elif self.numero in numeros_rojos:
            return Color.ROJO
        else:
            return Color.NEGRO
    
    @property
    def columna(self):
        return 0 if self.numero == 0 else (self.numero - 1) % 3 + 1
    
    @property
    def fila(self):
        return math.ceil(self.numero / 3)
    
    @property
    def docena(self):
        return math.ceil(self.numero / 12)
    
    @property
    def paridad(self):
        if self.numero == 0:
            return Paridad.CERO
        elif self.numero % 2 == 0:
            return Paridad.PAR
        else:
            return Paridad.IMPAR
    