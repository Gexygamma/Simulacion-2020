import math
import random as rnd

def middle_square(limit, seed=None):
    """
    Implementación del Método del Cuadrado Medio.

    Args:
        limit: Cantidad de iteraciones a realizar.
        seed: Semilla desde la cuál se parte la generación. Si no se
            especifica, se selecciona una al azar.
    """

    if seed is None:
        seed = rnd.randint(10**9, 10**10-1)
    elif seed < 0:
        raise ValueError("Seed must be a positive number ({0} was given).".format(str(seed)))
    print("MiddleSquare - Seed is:", seed)
    if limit < 0:
        raise ValueError("Limit must be a positive number ({0} was given).".format(str(limit)))
    count = 0
    size = int(math.log10(seed))+1 if seed > 0 else 1
    low_limit = int(size / 2)
    high_limit = low_limit + size
    while count < limit:
        seed = int(str(seed*seed).zfill(size*2)[low_limit:high_limit])
        count += 1
        yield seed
