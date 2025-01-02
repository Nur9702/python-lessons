#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:34:59 2025

@author: nurilla
"""

import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))
kvadrat = lambda x,y:x**y
print(kvadrat(3,2))

def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, "
      f"kubi {kub(3)} ga teng")
from math import sqrt # sonning kvadrat ildizini hisoblaydigan funktsiya
sonlar = list(range(11))
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)
def daraja2(x):
    """Berilgan sonning kv qaytaruvchi funktsiya"""
    return x*x
print(list(map(daraja2,sonlar)))

kvadratlar = list(map(lambda x:x*x,sonlar))
print(kvadratlar)
a = [5, 6, 7]
b = [8, 9, 10]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

import random as r
sonlar = r.sample(range(100),10)
print(sonlar)
def juftmi(x):
    """x juft bo'lsa True aks holda False qaytaruvchi funktsiya """
    return x%2==0
juft_sonlar = list(filter(juftmi,sonlar))
print(juft_sonlar)

juft_sonlar = list(filter(lambda x:x%2==0, sonlar))
print(juft_sonlar)

mevalar = ['olma', 'anor', 'nok', 'uzum', 'behi', 'qovun', 'banan', 'tarvuz', 'atir']
harf='o'
mevalar_b = list(filter(lambda meva:meva.startswith (harf),mevalar))
print(mevalar_b)

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)
mevalar3 = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(mevalar3)

class Kompyuter:
    def __init__(self, model, ram, hdd, gpu, cpu):
        self.model = model
        self.ram = ram
        self.hdd = hdd
        self.gpu = gpu
        self.cpu = cpu
        
    def info(self):
        inf = f"{self.model}, RAM:{self.ram}, SSD:{self.hdd}, CPU:{self.cpu}"
        return inf
        
macbook = Kompyuter("Apple Macbook Pro", "8GB", "512GB", "M1", "M1")