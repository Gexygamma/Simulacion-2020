def generar_reporte(test, gen, n, i, **kwargs):
    """
    Realiza una prueba estadística a un generador con parámetros por defecto
    e imprime los resultados.

    Args:
        test: La prueba estadística a realizar.
        gen: El generador a probar.
        n: Cantidad de números generados pseudoaleatoriamente.
        i: Cantidad de iteraciones de pruebas a realizar.
    """

    positive_results = 0
    for _i in range(i):
        if test(gen(n), **kwargs):
            positive_results += 1
    
    params = (key + "=" + str(value) for key, value in kwargs.items())
    header = test.__name__ + "(" + ",".join(params) + ")"

    print("{:>40} : {:f}".format(header, positive_results / i))
