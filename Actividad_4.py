#!/usr/bin/env python
# coding: utf-8

# ## Ejercicio 1
# 
# Crea una función llamada ejercicio1, que recibe la ruta donde se encuentra un dataset y devuelve una DataFrame con los datos que hay en el dataset. Para comprobar esta función utiliza el dataset `titanic.csv` que se incluye en esta actividad.

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


def ejercicio1(ruta):
    return pd.read_csv(ruta)


# In[ ]:


path = './titanic.csv'
df = ejercicio1(path)
len(df)


# In[ ]:


df.head()


# ## Ejercicio 2
# 
# Crea otra función llamada ejercicio2. Esta función recibe un único argumento que es un dataframe. En concreto debe recibir el dataframe que se ha obtenido de leer el dataset `titanic.csv`. Esta función devolverá otro dataset que incluya únicamente a los pasajeros menores de 35 años y que viajaban en 3ª clase.

# In[ ]:


def ejercicio2(dataframe):
    return dataframe[(dataframe['Age']<35) & (dataframe['Pclass'] == 3)]


# In[ ]:


df2 = ejercicio2(df)


# In[ ]:


df2


# ## Ejercicio 3
# 
# Crea una función llamada ejercicio3, que recibiendo como argumento el dataframe de salida del ejercicio 2, calcule el porcentaje de pasajeros menores de 35 años de 3ª clase que sobrevivieron.

# In[ ]:


def ejercicio3(dataframe):
    cuenta = dataframe.groupby(by='Survived').count()
    total = cuenta['PassengerId'][0] + cuenta['PassengerId'][1]
    return cuenta['PassengerId'][1]/total*100


# In[ ]:


ejercicio3(df2)


# ## Ejercicio 4
# 
# Implementa una función llamada ejercicio4 que recibiendo el dataframe con los datos del Titanic, devuelva en una tupla el porcentaje de hombres y mujeres que viajaban en el Titanic, redondeados al segundo decimal.

# In[ ]:


def ejercicio4(dataframe):
    per = (df.groupby(by='Sex').count().PassengerId / df.groupby(by='Sex').count().PassengerId.sum())*100
    roundper = round(per,2)
    return roundper[1], roundper[0]


# In[ ]:


ejercicio4(df)


# ## Ejercicio 5
# 
# 
# Implementa una función llamada ejercicio5 que recibiendo el dataframe con los datos del Titanic, devuelva en una lista el número de pasajeros que viajaban en 1ª, 2ª y 3ª clase.

# In[ ]:


def ejercicio5(dataframe):
    Passengers = df.groupby(by='Pclass').count().PassengerId
    return [Passengers.iloc[0], Passengers.iloc[1] , Passengers.iloc[2]]

