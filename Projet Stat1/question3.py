# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:56:34 2020


@author: Abdul Lahi Jaaw
"""

"""
Fatoumata Badji
Abdoulaye Diaw
Amsatou Diop

 Question 3: Données réelles
"""

# -*- 1- Enregistrements des données -*-
import pandas as pd

import numpy as np
df = pd.read_csv("smp.csv",decimal=",",delimiter=";" )
print(df)

print(df.dtypes)

# -*- 2- Changements des types de variables -*-
## Transposée du tableau
d = df.T
print(d)
print(d.dtypes)
## J'ai opté pour faire manuellement les chanements de variable pour éviter les problémes de keyError 
print(d.iloc[0]) 
a = d.iloc[1]
a = a.astype('category')
b = d.iloc[2]
b = b.astype('category')
c = d.iloc[3]
c = c.astype('category')
f = d.iloc[6]
f = f.astype('category')
g = d.iloc[7]
g = g.astype('category')
h = d.iloc[8]
h = h.astype('category')
i = d.iloc[9]
i = i.astype('category')
j = d.iloc[10]
j = j.astype('category')
k = d.iloc[11]
k = k.astype('category')
l = d.iloc[12]
l = l.astype('category')
m = d.iloc[13]
m = m.astype('category')
n = d.iloc[14]
n = n.astype('category')
o = d.iloc[15]
o = o.astype('category')
p = d.iloc[16]
p = p.astype('category')
q = d.iloc[17]
q = q.astype('category')
r = d.iloc[18]
r = r.astype('category')
s = d.iloc[19]
s = s.astype('category')
t = d.iloc[20]
t = t.astype('category')
u = d.iloc[21]
u = u.astype('category')
v = d.iloc[23]
v = v.astype('category')
w = d.iloc[24]
w = w.astype('category')
x = d.iloc[4]
x = x.astype('float64')
y = d.iloc[5]
y = y.astype('int64')
z = d.iloc[22]
z = z.astype('float64')
e = d.iloc[25]
e = e.astype('float64')
zz = d.iloc[0]
zz = zz.astype('float64')


print('âge         ',zz.dtypes)
print('prof         ',a.dtypes)
print('durée        ',b.dtypes)
print('discip       ',c.dtypes)
print('n.enfant     ',x.dtypes)
print('n.fratrie    ',y.dtypes)
print('ecole        ',f.dtypes)
print('séparation   ',g.dtypes)
print('juge.enfant  ',h.dtypes)
print('lieu         ',i.dtypes)
print('abus         ',j.dtypes)
print('grav.cons    ',k.dtypes)
print('dep.cons     ',l.dtypes)
print('ago.cons     ',m.dtypes)
print('ptsd.cons    ',n.dtypes)
print('alc.cons     ',o.dtypes)
print('subst. contre',p.dtypes)
print('scz.cons     ',q.dtypes)
print('char         ',r.dtypes)
print('rs           ',s.dtypes)
print('ed           ',t.dtypes)
print('dr           ',u.dtypes)
print('suicide.s    ',z.dtypes)
print('suicide.hr   ',v.dtypes)
print('suicide.past ',w.dtypes)
print('dur.interv   ',e.dtypes)


# -*- 3- Moyenne, Variance, Ecart type, 3 premiers quantiles -*-

## Moyenne
moyâge = np.mean(df.âge)## En utilisant notre dataframe
print('moyâge = ',moyâge)
moynenfant = np.mean(d.iloc[4])## Ici avec sa transposée 
print('moynenfant = ',moynenfant)
moynfratrie = np.mean(d.iloc[5])
print('moynfratrie = ',moynfratrie)
moydurinterv = np.mean(d.iloc[25])
print('moydurinterv = ',moydurinterv)

## Variance
varage = np. var(df.âge)
print('varage = ',varage)
varnenfant = np. var(d.iloc[4])
print('varnenfant = ',varnenfant)
varnfratrie = np. var(d.iloc[5])
print('varnfratrie',varnfratrie)
vardurinterv = np. var(d.iloc[25])
print('vardurinterv = ',vardurinterv)

## Ecart type
ectage = np.std(df.âge)
print('ectage = ',ectage)
ectnenfant = np.std(d.iloc[4])
print('ectnenfant = ',ectnenfant)
ectnfratrie = np.std(d.iloc[5])
print('ectnfratrie = ',ectnfratrie)
ectdurinterv = np.std(d.iloc[25])
print('ectdurinterv = ',ectdurinterv)

## Les 3 premiers quantiles de la variable age
Q1 = np.nanquantile(df.âge, [0.25])
print('Q1 = ',Q1)
Q2 = np.nanquantile(df.âge, [0.5])
print('Q2 = ',Q2)
Q3 = np.nanquantile(df.âge, [0.25])
print('Q3 = ',Q3)

# -*- 4- Boxplot pour la variable age -*-
df.boxplot(column="âge")

      # -*- Conclusion -*-
"""cette boîte à moustaches des ages indique que l'age médiane est de 37. 
L'age de la plupart des sujets est située entre 28 et 48,
mais l'age de certains sujets peut baisser jusqu'à 18 ou atteindre 83."""
       
# -*- 5- Données pour les agriculteurs qui ont plus de 2 enfants -*-
      
print(df.loc[d.iloc[4]>2,:])
      
      
# -*- 6- Fréquences des modalités de la variable prof, catégorie mondale -*-
effectifs = d.iloc[1].value_counts()
print(effectifs)
modalites = effectifs.index
print(modalites)
print('Fréquences = ',(effectifs.values) / len(df))

## Categorie modale
import statistics as stat
modprof = stat.mode(d.iloc[1])
print(' La categorie modale est: ',modprof)     
    
# -*- 7- Diagramme circulaire de la variable profession  -*-   
t = pd.crosstab(d.iloc[1], "f")
t.plot.pie(subplots=True, figsize = (6, 6))   
      
      
# -*- 8- Moyenne des ages par profession -*-
Moyape_prof=pd.crosstab(d.iloc[1],d.iloc[0],values=d.iloc[0],aggfunc=pd.Series.mean)
print(Moyape_prof)
      
      
      
# -*- 9- Table des effectifs pour les variables prof incluant les "NaN"  -*-
## Nous allons remplacer tous les NaN par "none"
dd =d.fillna("none")
print(dd)
effectif = dd.iloc[1].value_counts()
print(effectif)
      
        
# -*- 10- Nombre de "Nan" pour chaque variable -*-
Nbr_nan = effectif.loc["none"]
print('Nombre de Nan = ',Nbr_nan)      
      
# -*- 11-Suppression des lignes contenant des "nan" -*-
      
supp = df.dropna()
print(supp)      
      
      
# -*- 12_Histogramme et densité de la variable age sur la meme figure -*-

import seaborn

seaborn.distplot(supp.âge)
      
      
      
# -*- 13- Discretistaion de la variable age -*-
age_classe=pd.qcut(df.âge,5,labels=["min_age","Q1","Q2","Q3","max_age"])
print(age_classe)    
      
      
# -*- 14_ fréquences des modalités de la nouvelle variable age_classe -*-
effectifs = age_classe.value_counts()
modalites = effectifs.index 
tab = pd.DataFrame(modalites, columns = ["age_classe"]) 
tab["n"] = effectifs.values
tab["f"] = tab["n"] / len(age_classe) 
print(tab)

