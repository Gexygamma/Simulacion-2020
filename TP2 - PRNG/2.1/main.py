from archivos.generadores.lcg import lcg
from archivos.generadores.middle_square import middle_square
from archivos.test.chi_cuadrado import chi_cuadrado

if __name__ == "__main__":
    print("Prueba Chi-Cuadrado con LCG.")
    for _i in range(4):
        result = chi_cuadrado(lcg(100), 10)
        msg = "Pasó" if result else "Falló"
        print(msg)

    print("Prueba Chi-Cuadrado con cuadrado medio.")
    for _i in range(4):
        result = chi_cuadrado(middle_square(100), 10)
        msg = "Pasó" if result else "Falló"
        print(msg)
