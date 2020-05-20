from scipy.stats import ksone

def kolmogorov_smirnov(generador, a=0.05):
    """
    Implementación de prueba de kolmogorov-smirnov (frecuencia). Verifica si el
    generador no es rechazado según la hipotesis nula.

    Args:
        generador: Generador de nros aleatorios a probar.
        a: Nivel de significancia.
    """

    # Obtener muestra e inicializar variables.
    muestra = sorted(generador)
    tamaño_muestra = len(muestra)

    # Calcular D+ y D-, y obtenemos el mayor entre los dos. 
    d_max = max(((i+1)/tamaño_muestra - muestra[i]) for i in range(tamaño_muestra))
    d_min = min((muestra[i] - i/tamaño_muestra) for i in range(tamaño_muestra))
    d = max(d_max, abs(d_min))

    # Obtener valor crítico desde librería ("tabla").
    valor_critico = ksone.ppf(1-a/2, tamaño_muestra)

    return d < valor_critico
