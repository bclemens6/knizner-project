# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:21:11 2018

@author: Ben
"""

import numpy

ProspectWar0=2.0/600
WarAccrual=0.0

for i in range(100000):
    PWarMax=0.0
    for i in range(100):
        PWarFinal=numpy.random.normal()*1.1/550+numpy.random.normal()*1.1/550+ProspectWar0
        if PWarFinal>PWarMax:
            PWarMax=PWarFinal
    WarAccrual+=PWarMax*600

FinalWar=WarAccrual/100000.0
print(FinalWar)
        