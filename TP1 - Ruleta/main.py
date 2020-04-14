from archivos.graficador import graficar, graficar_multiples
from archivos.ingreso_datos import ingreso_iteraciones, ingreso_numero, ingreso_simulaciones
from archivos.simulacion import Simulacion

if __name__ == "__main__":

    iteraciones = ingreso_iteraciones()
    numero = ingreso_numero()
    cant_simulaciones = ingreso_simulaciones()

    simulacion = []

    simulacion.append(Simulacion())
    simulacion[0].ejecutar(iteraciones, numero)

    graficar(simulacion[0])

    for s in range(1, cant_simulaciones):
        simulacion.append(Simulacion())
        simulacion[s].ejecutar(iteraciones, numero)

    graficar_multiples(simulacion)

    # FORMATO LATEX y LINEAS DE FREC ESPERADA Y OTRAS ESPERADAS COSAS