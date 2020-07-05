
# coding: utf-8

# * El código del Ejercicio 5 estaba todo en un único fichero
# * Mover las funciones, variables, etc. que sean necesarias a un fichero llamado `lyrics.py`
# * Mover la definición de las canciones a `example_songs.py`
# * De forma que se pueda importar y ejecutar de la siguiente forma.

# In[1]:


import lyrics
import songs
words_clean = lyrics.split_into_words(songs.despacito)
#dudilla, cómo puedo prescindir del lyrics. sin tocar el codigo original? (que no incluye el import.) tengo que hacer un 
#.py que haga de main y llame a los demás con from x import x.y?

freqs = lyrics.words_to_frequencies(words_clean)

print("Palabras más frecuentes con más de 10 apariciones.")
print(lyrics.get_more_often_used_words(freqs))
print("\n")
print("Palabras más frecuentes con más de 5 apariciones.")
print(lyrics.get_more_often_used_words(freqs, threshold=5))

