from archivos.generadores.lcg import lcg
from archivos.generadores.middle_square import middle_square
from archivos.test.chi_cuadrado import chi_cuadrado
from archivos.test.kolmogorov_smirnov import kolmogorov_smirnov as kstest
from archivos.test.huecos import huecos
from archivos.test.corrida import corrida

def generar_reporte(test, gen, n, i):
    """
    Realiza una prueba estadística a un generador con parámetros por defecto
    e imprime los resultados.

    Args:
        test: La prueba estadística a realizar.
        gen: El generador a probar.
        n: Cantidad de números generados pseudoaleatoriamente.
        i: Cantidad de iteraciones de pruebas a realizar.
    """

    for _i in range(i):
        msg = "Pasó" if test(gen(n)) else "Falló"
        print(msg)

if __name__ == "__main__":
    print("~ Chi cuadrado ~")
    generar_reporte(chi_cuadrado, lcg, 100, 5)
    print("~ Kolmogorov-Smirnov ~")
    generar_reporte(kstest, lcg, 100, 5)
    print("~ Prueba de huecos ~")
    generar_reporte(huecos, lcg, 100, 5)
    print("~ Prueba de corridas ~")
    generar_reporte(corrida, lcg, 100, 5)
    print("~ Chi cuadrado ~")
    generar_reporte(chi_cuadrado, middle_square, 100, 5)
    print("~ Kolmogorov-Smirnov ~")
    generar_reporte(kstest, middle_square, 100, 5)
    print("~ Prueba de huecos ~")
    generar_reporte(huecos, middle_square, 100, 5)
    print("~ Prueba de corridas ~")
    generar_reporte(corrida, middle_square, 100, 5)
