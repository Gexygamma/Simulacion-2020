import random as rnd

def lcg(limit, seed=None, m=2**32, a=134775813, c=1):
    """
    Implementación del Generador Lineal Congruencial. (Nota: Como parámetros
    por defecto tomamos los usados en el lenguaje Pascal.)

    Args:
        limit: Cantidad de iteraciones a realizar.
        seed: Semilla desde la cuál se parte la generación. Si no se
            especifica, se selecciona una al azar.
        m: El operando módulo.
        a: El operando multiplicador.
        c: El operando incrementador.
    """

    if seed is None:
        seed = rnd.randint(10**9, 10**10-1)
    elif seed < 0:
        raise ValueError("Seed must be a positive number ({0} was given).".format(str(seed)))
    print("LCG - Seed is:", seed)
    if limit < 0:
        raise ValueError("Limit must be a positive number ({0} was given).".format(str(limit)))
    count = 0
    while count < limit:
        seed = (a * seed + c) % m
        count += 1
        yield seed
