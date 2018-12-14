# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:17:00 2018

@author: Ben
"""

import numpy
import statistics

YMWar2= 1.7/500
CKWar0=2/500
AKWar0=2/500
AYIter1=0.0
AYIter2=0.0
AKIter1=0.0
AKIter2=0.0
YMSDummy1=0.0
YMSDummy2=0.0
YMSIter1=0.0
YMSIter2=0.0

for i in range(1000000):
    YMFinal=numpy.random.normal()*1.1/550+numpy.random.normal()*1.1/550+YMWar2
    AKFinal=numpy.random.normal()*1.1/550+numpy.random.normal()*1.1/550+AKWar0
    CKFinal=numpy.random.normal()*1.1/550+numpy.random.normal()*1.1/550+CKWar0
    if YMFinal>max(AKFinal,CKFinal):
        YMSDummy1=max(AKFinal,CKFinal)
    else:
        YMSDummy1=min(AKFinal,CKFinal)
    if YMFinal>AKFinal:
        YMSDummy2=AKFinal
    else:
        YMSDummy2=0.0
    AllYadi1=max(YMFinal,AKFinal,CKFinal)*500+statistics.median([YMFinal,AKFinal,CKFinal])*150
    AllYadi2=max(YMFinal,AKFinal)*500+min(YMFinal,AKFinal)*150
    StartYadi1=max(YMFinal,AKFinal,CKFinal)*500+YMSDummy1*150
    StartYadi2=max(YMFinal,AKFinal)*500+YMSDummy2*150
    AKCKOnly=max(AKFinal,CKFinal)*500+min(AKFinal,CKFinal)*150
    AYIter1+=AllYadi1
    AYIter2+=AllYadi2
    YMSIter1+=StartYadi1
    YMSIter2+=StartYadi2
    AKIter1+=AKCKOnly
    AKIter2+=AKFinal*500
    

FinalYadi1=AYIter1/1000000.0
FinalYadi2=AYIter2/1000000.0
FinalYMS1=YMSIter1/1000000.0
FinalYMS2=YMSIter2/1000000.0
FinalAK1=AKIter1/1000000.0
FinalAK2=AKIter2/1000000.0
print(FinalYadi1)
print(FinalYadi2)
print(FinalYMS1)
print(FinalYMS2)
print(FinalAK1)
print(FinalAK2)