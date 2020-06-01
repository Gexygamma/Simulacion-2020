from scipy.stats import chi2
from math import floor

def chi_cuadrado(generador, n_interv=50, a=0.05):
    """
    Implementación de prueba de chi cuadrado (frecuencia). Verifica si el generador
    no es rechazado según la hipotesis nula.

    Args:
        generador: Generador de nros aleatorios a probar.
        n_interv: Cantidad de intervalos.
        a: Nivel de significancia.
    """

    # Obtener muestra e inicializar variables
    muestra = list(generador)
    n_obsv = len(muestra)
    gr_lib = n_interv - 1
    frec_esperada = n_obsv / n_interv
    
    # Poblar intervalos.
    intervalos = [0] * n_interv
    for elemento in muestra:
        index = floor(elemento * n_interv)
        intervalos[index] += 1

    # Calcular valor chi según fórmula.
    chi = sum(((frec_observada - frec_esperada)**2 / frec_esperada) \
        for frec_observada in intervalos)

    # Obtener valor crítico desde librería ("tabla").
    valor_critico = chi2.isf(q=a, df=gr_lib)

    return chi < valor_critico
