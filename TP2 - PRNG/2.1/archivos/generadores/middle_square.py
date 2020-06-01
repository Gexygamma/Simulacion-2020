import math
import random as rnd

from archivos.generadores._args import inicializar_semilla, manejar_excepciones

def middle_square(limit, seed=None, size=10):
    """
    Implementación del Método del Cuadrado Medio.

    Args:
        limit: Cantidad de iteraciones a realizar.
        seed: Semilla desde la cuál se parte la generación. Si no se
            especifica, se selecciona una al azar.
        size: Cantidad de dígitos que se arrastran a la siguiente
            iteración.
    """

    max_value = 10**size-1
    seed = inicializar_semilla(seed, max_value)
    manejar_excepciones(limit, seed, size)
    
    count = 0
    low_limit = int(size / 2)
    high_limit = low_limit + size
    while count < limit:
        seed = int(str(seed*seed).zfill(size*2)[low_limit:high_limit])
        count += 1
        # El nro es normalizado al rango [0,1] para simplificar las comparaciones.
        yield seed / max_value
