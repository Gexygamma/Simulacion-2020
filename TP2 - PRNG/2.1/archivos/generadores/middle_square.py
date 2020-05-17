import math
import random as rnd

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

    if seed is None:
        seed = rnd.randint(0, 10**size-1)
    elif seed < 0:
        raise ValueError("Seed must be a positive number ({0} was given).".format(str(seed)))
    if limit < 0:
        raise ValueError("Limit must be a positive number ({0} was given).".format(str(limit)))

    print("MiddleSquare - Semilla es:", seed)
    
    count = 0
    low_limit = int(size / 2)
    high_limit = low_limit + size
    while count < limit:
        seed = int(str(seed*seed).zfill(size*2)[low_limit:high_limit])
        count += 1
        # El nro es normalizado al rango [0,1] para simplificar las comparaciones.
        yield seed / (10**size-1)
