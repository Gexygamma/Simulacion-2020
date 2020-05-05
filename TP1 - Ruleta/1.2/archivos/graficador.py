import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
from numpy import ndarray

def graficar_frec(frec_relativa):
    plt.plot(frec_relativa)
    plt.ylabel('Frec. Rel. de la apuesta favorable')
    plt.ylim(-0.025, 1.025)
    plt.xlabel('Nro iteración')
    plt.show()

def graficar_simulacion(simulacion):
    _fig, ax = plt.subplots(ncols=len(simulacion.estrategias)+simulacion.graficar_tiradas)
    if type(ax) != ndarray:
        ax = [ax]
    for i, estrategia in enumerate(simulacion.estrategias):
        ax[i].plot(estrategia.rendimiento, label='Rendimiento')
        ax[i].plot(estrategia.apuesta, label='Apuesta')
        ax[i].plot(estrategia.barrera_absorcion, label='Barrera de Absorción', ls='dashdot')
        ax[i].set_title(str(estrategia))
        ax[i].legend(loc='upper left')
        ax[i].axhline(linewidth=.5, color='k')
        ax[i].set_ylabel('Capital')
        ax[i].set_xlabel('Número de tirada')
    if simulacion.graficar_tiradas:
        ax[-1].plot(simulacion.frec_absoluta_favorable)
        ax[-1].set_title('Secuencia de tiradas')
        ax[-1].axhline(linewidth=.5, color='k')
        ax[-1].set_xlabel('Número de tirada')
        ax[-1].set_ylabel('Racha')
    # plt.tight_layout()
    plt.show()
