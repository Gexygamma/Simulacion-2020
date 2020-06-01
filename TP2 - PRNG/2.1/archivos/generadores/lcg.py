import random as rnd

from archivos.generadores._args import inicializar_semilla, manejar_excepciones

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

    max_value = m - 1
    seed = inicializar_semilla(seed, max_value)
    manejar_excepciones(limit, seed, m, a, c)

    count = 0
    while count < limit:
        seed = (a * seed + c) % m
        count += 1
        # El nro es normalizado al rango [0,1] para simplificar las comparaciones.
        yield seed / max_value
