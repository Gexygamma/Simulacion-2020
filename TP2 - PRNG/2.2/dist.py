from enum import Enum, auto
from math import log, prod, exp
from random import random
import scipy.stats as st

class TipoDist(Enum):
    Continua = auto()
    Discreta = auto()

# Generadores de distribución continua.

class Uniforme(object):
    tipo = TipoDist.Continua
    scipy_name = "uniform"

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.params = a, b
    
    def generar(self):
        return self.a + (self.b - self.a) * random()
    
    def calc_valor_teorico(self, punto):
        return st.uniform.pdf(punto, loc=self.a, scale=self.b-self.a)

class Exponencial(object):
    tipo = TipoDist.Continua
    scipy_name = "expon"

    def __init__(self, lmbd):
        self.lmbd = lmbd
        self.params = (lmbd, )
    
    def generar(self):
        return -log(random()) / self.lmbd
    
    def calc_valor_teorico(self, punto):
        return st.expon.pdf(punto, scale=1/self.lmbd)

class Gamma(object):
    tipo = TipoDist.Continua
    scipy_name = "gamma"

    def __init__(self, k, lmbd):
        self.k = k
        self.lmbd = lmbd
        self.params = (lmbd, )
    
    def generar(self):
        p = prod(random() for _i in range(self.k))
        return -log(p) / self.lmbd
    
    def calc_valor_teorico(self, punto):
        return st.gamma.pdf(punto, self.k, scale=1/self.lmbd)

class Normal(object):
    tipo = TipoDist.Continua
    scipy_name = "norm"

    def __init__(self, em, std):
        self.em = em
        self.std = std
        self.params = em, std
    
    def generar(self):
        s = sum(random() for _i in range(12))
        return self.std * (s - 6) + self.em

    def calc_valor_teorico(self, punto):
        return st.norm(self.em, self.std).pdf(punto)

# Generadores de distribución discreta.

class Binomial(object):
    tipo = TipoDist.Discreta
    scipy_name = "binom"

    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.params = n, p
    
    def generar(self):
        return sum(random() <= self.p for _i in range(self.n))
    
    def calc_valor_teorico(self, punto):
        return st.binom.pmf(punto, self.n, self.p)

class Hipergeometrica(object):
    tipo = TipoDist.Discreta
    scipy_name = "hypergeom"

    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.k = k
        self.params = m, n, k
    
    def generar(self):
        total = self.m + self.n
        p = self.m / total
        x = 0
        for _i in range(self.k):
            s = int(random() <= p)
            x += s
            p = (total * p - s) / (total - 1)
            total -= 1
        return x

    def calc_valor_teorico(self, punto):
        return st.hypergeom.pmf(punto, self.m+self.n, self.m, self.k)

class Pascal(object):
    tipo = TipoDist.Discreta
    scipy_name = "nbinom"

    def __init__(self, k, p):
        self.k = k
        self.p = p
        self.params = k, p
    
    def generar(self):
        # return st.nbinom.rvs(self.k, self.p)
        pr = prod(random() for _i in range(self.k))
        return int(log(pr, 1-self.p))
    
    def calc_valor_teorico(self, punto):
        return st.nbinom.pmf(punto, self.k, self.p)

class Poisson(object):
    tipo = TipoDist.Discreta
    scipy_name = "poisson"

    def __init__(self, lmbd):
        self.lmbd = lmbd
        self.b = exp(-self.lmbd)
        self.params = (lmbd, )
    
    def generar(self):
        x = 0
        tr = random()
        while tr >= self.b:
            x += 1
            tr *= random()
        return x
    
    def calc_valor_teorico(self, punto):
        return st.poisson.pmf(punto, self.lmbd)

class Empirica(object):
    tipo = TipoDist.Discreta
    scipy_name = None

    def __init__(self, dist_emp_acum=None):
        self.dist_emp_acum = dist_emp_acum if dist_emp_acum else \
            [0.273, 0.31, 0.505, 0.514, 0.638, 0.696, 0.758, 0.909, 0.956]
    
    def generar(self):
        r = random()
        x = 0
        for p in self.dist_emp_acum:
            x += 1
            if r <= p:
                break
        else:
            x += 1
        return x
    
    def calc_valor_teorico(self, punto):
        dist_comp = self.dist_emp_acum.copy()
        dist_comp.insert(0, 0)
        dist_comp.append(1)
        return dist_comp[punto] - dist_comp[punto-1]
