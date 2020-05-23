from math import sqrt
from scipy.stats import norm
from archivos.utils import pairwise

def corrida(generador, a=0.05):
    """
    Implementación de prueba de corridas. Verifica si el generador no es rechazado
    según la hipotesis nula.

    Args:
        generador: Generador de nros aleatorios a probar.
        a: Nivel de significancia.
    """

    # Obtener generador de corridas de la muestra. Un paso ascendente está representado
    # con un "+", mientras que un paso descendente está representado con un "-".
    corridas = ("+" if a < b else "-" for a, b in pairwise(generador))

    # Contar cantidad de corridas.
    tamaño_muestra = 2 
    cant_corridas = 1
    paso_anterior = next(corridas)
    for paso in corridas:
        tamaño_muestra += 1
        if paso != paso_anterior:
            cant_corridas += 1
        paso_anterior = paso

    # Calcular media y variancia.
    media = (2*tamaño_muestra - 1) / 3
    variancia = (16*tamaño_muestra - 29) / 90

    # Estandarizar distribución normal.
    z0 = (cant_corridas - media) / sqrt(variancia)

    # Obtener valor crítico desde librería ("tabla").
    valor_critico = norm.ppf(q=1-a/2)

    return abs(z0) <= valor_critico