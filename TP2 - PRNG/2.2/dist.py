from math import log, prod, exp
from random import random

def uniforme(*, a, b):
    return a + (b - a) * random()

def exponencial(*, lmbd):
    return -log(random()) / lmbd

def gamma(*, k, lmbd):
    p = prod(random() for _i in range(k))
    return -log(p) / lmbd

def normal(*, em, std):
    s = sum(random() for _i in range(12))
    return std * (s - 6) + em

def pascal(*, k, q):
    p = prod(random() for _i in range(k))
    return int(log(p, q))

def binomial(*, n, p):
    return sum(random() <= p for _i in range(n))

def hipergeometrica(*, m, n, k):
    total = m + n
    p = m / total
    x = 0
    for _i in range(k):
        s = int(random() <= p)
        x += s
        p = (total * p - s) / (total - 1)
        total -= 1
    return x

def poisson(*, lmbd):
    b = exp(-lmbd)
    x = 0
    tr = random()
    while tr >= b:
        x += 1
        tr *= random()
    return x

def empirica():
    dist_emp_acum = [0.273, 0.31, 0.505, 0.514, 0.638, 0.696, 0.758, 0.909, 0.956]
    r = random()
    x = 0
    for p in dist_emp_acum:
        x += 1
        if r <= p:
            break
    else:
        x += 1
    return x
