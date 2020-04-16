# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:16:51 2020

@author: Abdul Lahi Jaaw
"""

# -*- coding: utf-8 -*-
"""
 Abdoulaye Diaw
 Question 2 : Regression linéairre
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 


def enregistrementdonnees():
    print('--ENREGISTREMENT\
          Nous avons opté d écrire les données sous formats csv quon va importer grace à pandas')
    donnees=pd.read_csv('stat.csv')
    print(donnees)



    

def representationdesxiyi():
    plt . scatter ( xi , yi, color='black', marker = '*', label='(xi,yi)')
    plt . xlabel (" X ", color='r')
    plt . ylabel (" Y ",color='r')
    plt . title (" Représentation des yi en fonction des xi ",color='r')
    plt.legend()
    plt.show()
    print('A la vue de cette representation, on ne peut pas supçonner une liason linéaire')
  
    
#Pour etudier la regression linéaire, nous introduisons la notion de
#convariance (d'un couple de variables) puis le coefficient de correlation lineaire
#(un indice de covariation linéaire des deux variables)


def cov(X, Y): 
    sum = 0 
    for j in range(0, len(X)): 
        sum += (X[j]) * (Y[j])
    return (sum/(len(X)))-moyenneX*moyenneY


xi=[18, 7, 14, 31, 21, 5, 11, 16, 26, 29]
yi=[55, 17, 36, 85, 62, 18, 33, 41, 63, 87]
X = np.array(xi)
Y = np.array(yi)
moyenneX=X.mean() 
moyenneY=Y.mean() 
varianceX=X.var()
varianceY=Y.var()
ecartypeX=X.std()
ecartypeY=Y.std()
covariance=cov(X,Y)
r=covariance/(ecartypeX*ecartypeY)
a=covariance/varianceX
b=moyenneY-a*moyenneX
Z= a*X+ b



def droitedesmoindrescarrés():
    print('Détermination de la droite des moindres carré')     
    print('Soit Z, la droite des moindres carrés telle que Z= aX + B')
    r=covariance/(ecartypeX*ecartypeY)
    a=covariance/varianceX
    b=moyenneY-a*moyenneX
    Z= a*X+ b
    print('La valeur de a est ', a)
    print('La valeur de b est ', b)
    return a*X+ b


def cov(X, Y): 
    sum = 0 
    for j in range(0, len(X)): 
        sum += (X[j]) * (Y[j])
    return (sum/(len(X)))-moyenneX*moyenneY


def ordonnéesdesyiparZ():
    print('Les ordonnées des yi calculés par la droite des moindres carrés correspondant aux différentes valeurs des xi')
    print(Z)


def droitesurmemegraphe():
    plt.plot(X, Z, color='b', label='Droitemoncarré')
    plt . scatter ( xi , yi, color='black', marker = '*', label='(xi,yi)')
    plt . xlabel (" X ", color='r')
    plt . ylabel (" Y ",color='r')
    plt . title (" Représentation des yi en fonction des xi et de la droite",color='r')
    plt.legend()
    plt.show()


def estimation():
    Z21=(2.734756097560975)*21+1.0213414634146503 
    print('Une estimation plausible de Y à xi = 21 est ')
    print(Z21)    
Z21=(2.734756097560975)*21+1.0213414634146503


def ecartval():   
    ecart=Y[4]-Z21
    print('Lecart entre les deux valeurs de Y appellé RESIDUS est de ',ecart)
        


def pointmoyen():
    plt.plot(X, Z, color='b', label='Droitemoncarré')
    plt . scatter ( xi , yi, color='black', marker = '*', label='(xi,yi)')
    plt . scatter ( moyenneX , moyenneY, color='red', marker = 'o', label=( '(¯x, y¯) '))
    plt . xlabel (" X ", color='r')
    plt . ylabel (" Y ",color='r')
    plt . title (" Représentation des yi en fonction des xi et de la droite",color='r')
    plt.legend()
    plt.show()
    print('Oui la droite des moindres carrés obtenue en 2 passe par le point moyen (moyenneX,moyenneY)')
    print('La droite de régression linéaire passe par le point moyen car la droite se determine à laide de ces variables')

enregistrementdonnees()
representationdesxiyi() 
droitedesmoindrescarrés()
ordonnéesdesyiparZ()
droitesurmemegraphe()
estimation()
ecartval()
pointmoyen()