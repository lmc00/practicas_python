
# coding: utf-8

# # Ejercicio
# 
# Adaptado de http://www.scipy-lectures.org/index.html
# 
# En el fichero `data/populations.txt` se describe la población de liebres, linces y zanahoras en Canada desde 1900 a 1920.
# 
# Se pide:
# * Calcular la media para cada una de las poblaciones.
# * Calcular la desviación estándar para cada una de las poblaciones.
# * ¿Qué población tuvo la mayor población cada año?
# 
# Recordad, documentación `numpy.ndarray`: https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html

# In[5]:


# Podemos ver el fichero directamente con el comando de Jupyter !cat

get_ipython().system('cat data/populations.txt')


# In[6]:


import numpy


# In[7]:


data = numpy.loadtxt("data/populations.txt")
data


# In[80]:


# Calcular la media para cada una de las especies
#la poblacion de cada especie cada año es una columna
media=data.mean(axis=0)
#no queremos para nada hacer media de los años, eso no tiene sentido
media_liebres=media[1]
media_linces=media[2]
media_zanahorias=media[3]
print("La media de liebres es:")
print(media_liebres)
print()
print("La media de linces es:")
print(media_linces)
print()
print("La media de zanahorias es:")
print(media_zanahorias)


# In[81]:


# Calcular la desviación estándar para cada una de las especies
#Es casi el mismo código, sólo que en vez de mean ahora es std y lo demás todo igual
desviacion_std=data.std(axis=0)
#no queremos para nada hacer media de los años, eso no tiene sentido
desviacion_std_liebres=desviacion_std[1]
desviacion_std_linces=desviacion_std[2]
desviacion_std_zanahorias=desviacion_std[3]
print("La desviacion estándar de liebres es:")
print(desviacion_std_liebres)
print()
print("La desviación estándar de linces es:")
print(desviacion_std_linces)
print()
print("La desviación estándar de zanahorias es:")
print(desviacion_std_zanahorias)


# In[40]:


#Ahora voy a calcular la desviación estándar a pelo para un caso simplemente por comparar
prueba_desviacion = data.copy() #para no tocar nada y liarla
poblacion_liebres=prueba_desviacion[:,1] 
media_prueba_liebres=poblacion_liebres.mean()
sumatorio = 0
for i in poblacion_liebres:
    diferencia = i-media_prueba_liebres
    sumatorio = sumatorio + diferencia**2
desviacion_tipica = sumatorio/len(poblacion_liebres)
desviacion_estandar = desviacion_tipica**0.5
print(desviacion_estandar)
#se obtiene 20897.906458089667
#parece que todo ok!


# In[79]:


# ¿Qué especie tuvo la población mayor cada año?
#las poblaciones están en las columnas 1 2 y 3. Cada fila es un año, así que quiero primero obtener el máximo de cada fila, y luego sacar por pantalla con qué especie se corresponde el máximo
#es útil numpy.where(condicion), que retorna donde se da esa igualdad en el array.
#También vale argmax(axis=0)(retorna la posición en cada columna empezando a contar por 0 del máximo)o con axis =1 para saber en qué posición de la fila está el máximo de la fila
poblaciones = data[:,1:4] #para que el atributo argmax no vaya y me pueda seleccionar el año como el máximo valor
posicion_maximo_fila = poblaciones.argmax(axis=1) #genero array en el que cada elemento es la posicion en el que se encuentra
año = data[:,0:1]
año_editable = año.copy() #para no tocar los raw data
año_editable = año_editable.astype('int32') #sólo para sacarlo en int, que parece más lógico siendo un año
#la poblacion maxima de cada año. Ejemplo: si en 1910 (la primera entrada) fueron las liebres la especie con mayor poblacio
#el primer elemento del array sera un 0, si en 1912 fueron las zanahorias, el tercer elemento sera un 2 etc
print("el maximo de poblacion en cada año ha sido para la especie:")
for i in range (0,21):
    print(año_editable[i])
    if posicion_maximo_fila[i] == 0:
        print("Liebre")
    if posicion_maximo_fila[i] == 1:
        print("lince")
    if posicion_maximo_fila[i] ==2:
        print("zanahoria")
    print()
    


