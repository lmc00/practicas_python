
# coding: utf-8

# In[12]:


import lyrics_processor.frequencies
import lyrics_processor.process
from lyrics_processor import songs
despacito = lyrics_processor.songs.example.despacito
words_clean = lyrics_processor.process.split_into_words(despacito)
freqs=lyrics_processor.process.words_to_frequencies(words_clean)
print("Palabras más frecuentes con más de 10 apariciones.")
print(lyrics_processor.frequencies.get_more_often_used_words(freqs))
print()
print("Palabras más frecuentes con más de 5 apariciones.")
print(lyrics_processor.frequencies.get_more_often_used_words(freqs, threshold=5))



