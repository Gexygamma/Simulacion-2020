def ingreso_iteraciones():
    while True:
        try:
            iteraciones = int(input('Ingrese cantidad de iteraciones: '))
        except ValueError:
            print('Ingreso con formato incorrecto.')
        else:
            if iteraciones <= 0:
                print('Cantidad de iteraciones debe ser mayor a cero.')
            else:
                break
    return iteraciones

def ingreso_numero():
    while True:
        try:
            numero = int(input('Ingrese número a analizar (0-36): '))
        except ValueError:
            print('Ingreso con formato incorrecto.')
        else:
            if not 0 < numero < 36:
                print('Número ingresado fuera de rango.')
            else:
                break
    return numero

def ingreso_simulaciones():
    while True:
        try:
            cant_simulaciones = int(input('Ingrese cantidad de simulaciones: '))
        except ValueError:
            print('Ingreso con formato incorrecto.')
        else:
            if cant_simulaciones <= 0:
                print('Cantidad de simulaciones debe ser mayor a cero.')
            else:
                break
    return cant_simulaciones