
# coding: utf-8

# El programa del ejercicio 3 que calculaba las palabras más utilizadas se puede reescribir de forma mucho más sencilla utilizando un `pandas`.
# 
# Para ello, en lugar de devolver un diccionario en la función `words_to_frequencies` se puede devolver una `Series` de Pandas.

# In[36]:


import numpy
import pandas


# In[37]:


# Leemos el fichero

lyrics = open("data/despacito.txt", "r").read()


# In[38]:


def split_into_words(lyrics):
    """
    Split a string into lowercase words, removing all punctuation characters,
    returning the result.
    """
    result = []
    for word in lyrics.lower().split():  # lower() convierte las palabras en minusculas
        word = word.strip(',.;()"!')  # strip() elimina del incio y del final los caracteres que le pasemos
        result.append(word)
    return result


# In[39]:


def words_to_frequencies(lyrics):
    """
    Convert words into frequencies. Return a pandas.Series whose keys are the
    words with the frequency as the value
    """
    freqs = pandas.Series()
    for word in lyrics:
        if word in freqs:
            freqs[word] += 1 #este comando funciona igual con una Series de pandas que con biblioteca
        else:
            freqs[word] = 1
        # Alternativa al if anterior
        # freqs[word] = freqs.get(word, 0) + 1
        # Otra alternativa
        # freqs.setdefault(word, 0)
        # freqs[word] += 1
    return freqs


# In[46]:


def get_more_often_user_words(frequencies,a, threshold=10):
    """
    Se le pasa la Series de Pandas generada con words_to_frequencies, retorna lista con las palabras que cumplen el threshold
    POR ENCIMA DEL NÚMERO DE THRESHOLD, NO IGUAL AL MISMO
    Return a list of the words that are used more often, above
    the *optional* threshold. If no threshold is passed, use 10.
    """
    result= frequencies[frequencies>threshold] #añado a la lista de result un único elemento
    #que es la serie de pandas que tenía todas las palabras con su conteo pero filtrada con el mínimo
    #de repeticiones que exijo.
    #Actualización: ahora directamente retorno la serie pandas, no tiene mucho sentido meterla
    #dentro de una lista por mucho que la documentación que viene por defecto (que supongo que se deba a que es copy paste del 3.2)
    #lo pida. Es más eficiente sacar un pandas. Siempre puedes copiar todos los elementos de la serie
    # a una lista, pero es innecesario para lo requerido en el ejercicio.
    
    
    
    
    return result


# In[50]:


words_clean = split_into_words(lyrics)

freqs = words_to_frequencies(words_clean)

print("Palabras más frecuentes con más de 10 apariciones.")
print(get_more_often_user_words(freqs))
print("\n")

print("Palabras más frecuentes con más de 5 apariciones.")
print(get_more_often_user_words(freqs,1, threshold=5))

