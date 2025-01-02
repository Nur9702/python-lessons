#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:38:01 2025

@author: nurilla
"""

import hello
avto1 = hello.avto_info('gm', 'jentra', 'oq', 'avtomat',2022, 15000)
hello.info_print(avto1) 

import hello as aim
avto1 = aim.avto_info('gm', 'jentra', 'oq', 'avtomat',2022, 15000)
aim.info_print(avto1) 

from hello import avto_info, info_print
avto1 = avto_info('gm', 'jentra', 'oq', 'avtomat',2022, 15000)
info_print(avto1)

from hello import avto_info as ainfo, info_print as iprint

avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
iprint(avto1)

from untitled0 import *
avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)

import math

x=400
print(math.sqrt(x))
print(math.pow(5, 3))
print(math.pi)
print(math.log2(8))
print(math.log10(100))

import random as r # random modulini r deb chaqirayapmiz

son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
print(son)
ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

x = list(range(0,51,5))
print(x)
print(r.choice(x))

#shuffle
x = list(range(11))
print(x)
r.shuffle(x)
print(x)

        






