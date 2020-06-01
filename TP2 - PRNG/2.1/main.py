from archivos.generadores.lcg import lcg
from archivos.generadores.middle_square import middle_square
from archivos.generadores.otros import random_python, secrets_python
from archivos.test.chi_cuadrado import chi_cuadrado
from archivos.test.kolmogorov_smirnov import kolmogorov_smirnov as kstest
from archivos.test.huecos import huecos
from archivos.test.corrida import corrida
from archivos.reporte import generar_reporte

if __name__ == "__main__":
    nros_gen = 10000
    pruebas = 2500
    print("~ LCG ~")
    generar_reporte(chi_cuadrado, lcg, nros_gen, pruebas, a=0.02)
    generar_reporte(kstest, lcg, nros_gen, pruebas, a=0.02)
    generar_reporte(corrida, lcg, nros_gen, pruebas, a=0.02)
    generar_reporte(huecos, lcg, nros_gen, pruebas, a=0.02)
    print("~ Middle Square ~")
    generar_reporte(chi_cuadrado, middle_square, nros_gen, pruebas, a=0.02)
    generar_reporte(kstest, middle_square, nros_gen, pruebas, a=0.02)
    generar_reporte(corrida, middle_square, nros_gen, pruebas, a=0.02)
    generar_reporte(huecos, middle_square, nros_gen, pruebas, a=0.02)
    print("~ Random (Python 3.8.1) ~")
    generar_reporte(chi_cuadrado, random_python, nros_gen, pruebas, a=0.02)
    generar_reporte(kstest, random_python, nros_gen, pruebas, a=0.02)
    generar_reporte(corrida, random_python, nros_gen, pruebas, a=0.02)
    generar_reporte(huecos, random_python, nros_gen, pruebas, a=0.02)
    print("~ Secrets (Python 3.8.1) ~")
    generar_reporte(chi_cuadrado, secrets_python, nros_gen, pruebas, a=0.02)
    generar_reporte(kstest, secrets_python, nros_gen, pruebas, a=0.02)
    generar_reporte(corrida, secrets_python, nros_gen, pruebas, a=0.02)
    generar_reporte(huecos, secrets_python, nros_gen, pruebas, a=0.02)
