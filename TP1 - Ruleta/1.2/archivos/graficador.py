import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

def graficar_frec(frec_relativa):
    plt.plot(frec_relativa)
    plt.ylabel('Frec. Rel. de la apuesta favorable')
    plt.ylim(-0.025, 1.025)
    plt.xlabel('Nro iteración')
    plt.show()

def graficar_simulacion(simulacion):
    _fig, ax = plt.subplots(ncols=len(simulacion.estrategias))
    for i, estrategia in enumerate(simulacion.estrategias):
        ax[i].plot(estrategia.rendimiento, label='Rendimiento')
        ax[i].plot(estrategia.apuesta, label='Apuesta')
        ax[i].plot(estrategia.barrera_absorcion, label='Barrera de Absorción', ls='dashdot')
        ax[i].set_title(str(estrategia))
        ax[i].legend(loc='upper left')
        ax[i].axhline(linewidth=.5, color='k')
        ax[i].set_ylabel('Capital')
        ax[i].set_xlabel('Número de tirada')
    plt.tight_layout()
    plt.show()
