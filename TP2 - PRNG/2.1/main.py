from archivos.generadores.lcg import lcg
from archivos.generadores.middle_square import middle_square

if __name__ == "__main__":
    for i in lcg(5):
        print(i)
    
    for i in middle_square(5):
        print(i)
