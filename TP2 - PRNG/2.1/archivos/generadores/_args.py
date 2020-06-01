from random import randint

def manejar_excepciones(*args):
    for i, arg in enumerate(args):
        if not (isinstance(arg, int) and arg >= 0):
            raise ValueError("Incorrect argument value on pos {0}.".format(i))

def inicializar_semilla(seed, max_value):
    if seed is None:
        seed = randint(0, max_value)
    return seed