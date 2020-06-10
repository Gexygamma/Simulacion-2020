import dist 
import matplotlib.pyplot as plt

tamaño_muestra = 100000

def mostrar_continua(dist, **kwargs):
    data = [dist(**kwargs) for _i in range(tamaño_muestra)]
    plt.hist(data, bins=50, density=True)
    plt.show()

def mostrar_discreta(dist, **kwargs):
    data = [dist(**kwargs) for _i in range(tamaño_muestra)]
    md = min(data)
    x = [n for n in range(md, max(data) + 1)]
    y = [0] * len(x)
    for point in data:
        y[point-md] += 1
    for i in range(len(y)):
        y[i] /= len(data)
    plt.bar(x, y, tick_label=x)
    plt.show()

if __name__ == "__main__":
    # mostrar_xxx(distribucion, argumentos)
    mostrar_discreta(dist.binomial, n=10, p=0.5)
