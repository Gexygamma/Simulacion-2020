from math import floor
from scipy.stats import ksone
from archivos.utils import pairwise

def huecos(generador, base=10, a=0.05):
    """
    Implementación de prueba de huecos. Verifica si el generador no es rechazado
    según la hipotesis nula.

    Args:
        generador: Generador de nros aleatorios a probar.
        base: Base múltiplicadora. Los nros se testearan en el rango [0,base).
        a: Nivel de significancia.
    """

    # Obtener muestra escalada por un factor base.
    muestra = [min(floor(i*base), base-1) for i in generador]

    # Calcular frecuencia absoluta de cada tamaño de hueco.
    frec_abs = {}
    for nro in range(base):
        posiciones = [index for index, elemento in enumerate(muestra) if elemento == nro]
        for hueco in pairwise(posiciones):
            tamaño_hueco = hueco[1] - hueco[0] - 1
            frec_abs[tamaño_hueco] = frec_abs.get(tamaño_hueco, 0) + 1

    # Calcular frecuencia absoluta acumulada.
    frec_abs_acum = [frec_abs.get(0, 0)]
    for tamaño_hueco in range(1, max(frec_abs.keys())+1):
        frec_abs_acum.append(frec_abs_acum[-1] + frec_abs.get(tamaño_hueco, 0))

    # Calcular frecuencia relativa acumulada.
    frec_rel_acum = []
    for frec in frec_abs_acum:
        frec_rel_acum.append(frec / frec_abs_acum[-1])
    
    # Calcular diferencia con la frecuecia relativa acumulada esperada.
    n_interv = len(frec_rel_acum)
    frec_esp = [1-(1-1/base)**(x+1) for x in range(n_interv)]
    d = max(abs(frec_rel_acum[i] - frec_esp[i]) for i in range(n_interv))

    # Calcular diferencia de confiabilidad.
    d_conf = ksone.ppf(1-a/2, len(muestra))

    return d < d_conf
