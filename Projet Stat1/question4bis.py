# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:16:51 2020

@author: Abdul Lahi Jaaw
"""

# -*- coding: utf-8 -*-
"""
 Abdoulaye Diaw
 Fatoumata Badji
 Amsatou Diop
 Question 4: Methode de Monte Carlo
"""


import random         
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
def estimation_de_I2(I, Val_estim, b, n):   
    somme = 0                   
    for i in range(0, n):       
        x = random.uniform(Val_estim, b)
        somme += I2(x)
        
    return somme / n
I2=lambda x: sqrt(1-x**2)

valestin=0
Val_estim=estimation_de_I2(I2,valestin,1,10000)
print("une estimation de I2 pour n=10000 donne",Val_estim)

#Nombre de flechettes lanchées dans le carré unite
n=[10,100,500,1000,5000,10000]
valn=np.array(n)

def observ_suivant_val_n():
    

    for i in range(6):
        valeurnchoisie=n[i]
        print(valeurnchoisie)
        x=np.random.uniform(low=0, high=1, size=[valeurnchoisie,1])
        y=np.random.uniform(low=0, high=1, size=[valeurnchoisie,1])
        plus=y<=np.sqrt(1-x**2)
        pie_sur4=np.sum(plus)/valeurnchoisie
        print("la veur estimée de ¶/4:", pie_sur4,"POUR n=",valeurnchoisie)
        

        xplus=x[plus]
        yplus=y[plus]
        plt.figure(figsize=[5,5])
        plt.scatter(x, y, color='orange')
        plt.scatter(xplus,yplus, color='blue')
        plt.show()

observ_suivant_val_n()