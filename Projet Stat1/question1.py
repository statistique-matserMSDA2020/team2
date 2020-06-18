# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:56:34 2020


@author: Abdul Lahi Jaaw
"""

"""
Fatoumata Badji
Abdoulaye Diaw
Amsatou Diop

 Question 1: Données réelles
"""

import numpy.random 
import matplotlib.pyplot as plt
from math import *
import numpy as np
from scipy.stats import gamma

"""loi binomiale"""
nbin=10000                              
X=numpy.random.binomial(30,0.2,nbin)              
print('Notre echantillon obtenu',X)
plist=[0]*30
for i in range(1,30):
    plist[i]=X.tolist().count(i)/nbin    
plt.hist(X,bins=15,color='blue',density=True, edgecolor="k")
plt.title("Echantillon de taille 10000 suivant une loibinomiale B(30,0.2)")
plt.show()

"""loi normale"""

nnorm=10000
simu=numpy.random.normal(3,.4,size=nnorm)
x=np.linspace(-10, 20, 200)
k=1/(2*sqrt(2*pi))
l=(-1/8)*((x-3)**2)
print(k)
puissance=np.exp(l)
y=k*puissance
plt.figure()
plt.plot(x,y, color='red',label='loi normale')
plt.title('Echantillon de taille 10000 suivant une loi normale N(3,.4)')
plt.show()


"""loi gama"""

gamma_distribution = gamma(10,10,.5)
x = np.linspace(-10, 30, 10000)
plt.plot(x, gamma_distribution.pdf(x), 'y')
plt.title(' un échantillon de taille 10000 suivant une loi gamma γ(10,.5).')
plt.show()

