import random
import secrets

from archivos.generadores._args import manejar_excepciones

def random_python(limit, seed=None):
    if seed is None:
        random.seed()
    elif seed >= 0:
        random.seed(seed)
    
    manejar_excepciones(limit)
    
    count = 0
    while count < limit:
        count += 1
        yield random.random()
    
def secrets_python(limit, bits=64):
    manejar_excepciones(limit, bits)
    
    max_value = 2**bits
    count = 0
    while count < limit:
        count += 1
        yield secrets.randbits(bits) / max_value
