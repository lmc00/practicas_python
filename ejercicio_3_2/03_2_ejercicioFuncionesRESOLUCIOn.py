
# coding: utf-8

# El siguiente programa imprime por pantalla las palabras más frecuentes
# que se encuentre en una cadena de caracteres, en este caso una canción.
# Sin embaro, tiene varios errores, tanto de sintaxis, como de ejecución,
# como de funcionalidad.

# In[20]:


lyrics = """Ay
Fonsi
DY
Oh
Oh no, oh no
Oh yeah
Diridiri, dirididi Daddy
Go
Sí, sabes que ya llevo un rato mirándote
Tengo que bailar contigo hoy (DY)
Vi que tu mirada ya estaba llamándome
Muéstrame el camino que yo voy (Oh)
Tú, tú eres el imán y yo soy el metal
Me voy acercando y voy armando el plan
Solo con pensarlo se acelera el pulso (Oh yeah)
Ya, ya me está gustando más de lo normal
Todos mis sentidos van pidiendo más
Esto hay que tomarlo sin ningún apuro
Despacito
Quiero respirar tu cuello despacito
Deja que te diga cosas al oído
Para que te acuerdes si no estás conmigo
Despacito
Quiero desnudarte a besos despacito
Firmo en las paredes de tu laberinto
Y hacer de tu cuerpo todo un manuscrito (sube, sube, sube)
(Sube, sube)
Quiero ver bailar tu pelo
Quiero ser tu ritmo
Que le enseñes a mi boca
Tus lugares favoritos (favoritos, favoritos baby)
Déjame sobrepasar tus zonas de peligro
Hasta provocar tus gritos
Y que olvides tu apellido (Diridiri, dirididi Daddy)
Si te pido un beso ven dámelo
Yo sé que estás pensándolo
Llevo tiempo intentándolo
Mami, esto es dando y dándolo
Sabes que tu corazón conmigo te hace bom, bom
Sabes que esa beba está buscando de mi bom, bom
Ven prueba de mi boca para ver cómo te sabe
Quiero, quiero, quiero ver cuánto amor a ti te cabe
Yo no tengo prisa, yo me quiero dar el viaje
Empecemos lento, después salvaje
Pasito a pasito, suave suavecito
Nos vamos pegando poquito a poquito
Cuando tú me besas con esa destreza
Veo que eres malicia con delicadeza
Pasito a pasito, suave suavecito
Nos vamos pegando, poquito a poquito
Y es que esa belleza es un rompecabezas
Pero pa montarlo aquí tengo la pieza
Despacito
Quiero respirar tu cuello despacito
Deja que te diga cosas al oído
Para que te acuerdes si no estás conmigo
Despacito
Quiero desnudarte a besos despacito
Firmo en las paredes de tu laberinto
Y hacer de tu cuerpo todo un manuscrito (sube, sube, sube)
(Sube, sube)
Quiero ver bailar tu pelo
Quiero ser tu ritmo
Que le enseñes a mi boca
Tus lugares favoritos (favoritos, favoritos baby)
Déjame sobrepasar tus zonas de peligro
Hasta provocar tus gritos
Y que olvides tu apellido
Despacito
Vamos a hacerlo en una playa en Puerto Rico
Hasta que las olas griten "¡ay, bendito!"
Para que mi sello se quede contigo
Pasito a pasito, suave suavecito
Nos vamos pegando, poquito a poquito
Que le enseñes a mi boca
Tus lugares favoritos (favoritos, favoritos baby)
Pasito a pasito, suave suavecito
Nos vamos pegando, poquito a poquito
Hasta provocar tus gritos
Y que olvides tu apellido (DY)
Despacito
"""


# In[28]:


#le he añadido a los parametros de .strip el ? y ¿ ya que aunque no cambia en elcódigo, mejora
#la generalidad
def split_into_words(lyrics): #retorna lista con las palabras en minúsula y sin signos de puntuación
    """
    Split a string into lowercase words, removing all punctuation characters,
    returning the result.
    """
    result = []
    for word in lyrics.lower().split():  # lower() convierte las palabras en minusculas
        palabra = word.strip(',.;()"¡!?¿')  # strip() elimina del incio y del final los caracteres que le pasemos
        result.append(palabra) #he cambiado word por palabra, que no es necesario pero simplemente para hacer más visual la distinción
        #entre el elemento que sirve par iterar y el resto
    return result
    


# In[18]:


def words_to_frequencies(lyrics): #le pasas lista con las palabras tras aplicar split_into_words y te retorna biblioteca con el conteo
    """
    Convert words into frequencies. Return a dictionary whose keys are the
    words with the frequency as the value
    """
    freqs = {}
    for word in lyrics:
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1
        # Alternativa al if anterior
        # freqs[word] = freqs.get(word, 0) + 1 #lo de (word,0) es porque el get tiene un argumento opcional
        #que se retorne dicho argumento en caso de no encontrar esa key
        # Otra alternativa
        # freqs.setdefault(word, 0)
        # freqs[word] += 1
    return freqs


# In[4]:


def most_common_words(frequencies): #le pasas biblioteca que obtienes de words_to_frequencies y retorna tupla
  #con el numero de repeticiones como primer elemento y la lista de las palabras que tienen tantas repeticiones como segundo elemento
    """
    Return a tuple containing:
    * The number of occurences of a word in the first tuple element
    * A list containing the words with that frequency
    """
    values = frequencies.values() #inciso, .values() retorna una lista con todos los valores
    #de una biblioteca en lista
    best = max(values)
    
    words = []
    for word, score in frequencies.items():
        if score == best:
            words.append(word)
    return (best, words)
  #puedes cuando llames al método pedir que te guarde el resultado en una referencia,
  #en ese caso tendrás una tupla del tipo (2, ['hola']). (el segundo elemento de la tupla es una lista pero ya queda inmodificable
  #por ser parte e una tupla, o eso creo)
  #también puedes igualarlo a dos cosas y en una te guarda el 2 y en otra el [palabras] que es una lista
  #NOTA QUE PUEDES METER TUPLA EN LISTA Y LISTA EN TUPLA


# In[19]:


def get_more_often_used_words(frequencies, threshold=10):
    """
    Return a list of the words that are used more often, above
    the *optional* threshold. If no threshold is passed, use 10.
    """
    frecuencia=frequencies.copy()#con esto ya no toco la libreria de fuera de la funcion y no doy problema si la llamo más veces
    result = []
    while True:
        score = most_common_words(frecuencia) 
        if score[0] <= threshold: #faltaba un = y por eso no cribaba las que tocaban (dejaba las del threshold cuando se supone que no debe)
            break
        for w in score[1]:
            del frecuencia[w] #del toca la palabra w y su valor de la biblioteca frecuencia
            #aqui se ve que está tocando una variable mutable como es frequencies
            #que además se usa posteriormente y está fuera de la función,
            #por eso se carga las frecuencias esas y luego en el codigo original cuando 
            #llama a este metodo por segunda vez con threshold 5, lo que está por encima de 10
            #no sale, se lo ha cargado antes. Además cuidadito con una libreria en la que tengas dentro objetos que la lias
            result.append(score)
        
    return result


# In[29]:


words_clean = split_into_words(lyrics)

freqs = words_to_frequencies(words_clean)

print("Palabras más frecuentes con más de 10 apariciones.") #el programa que nos viene de
#base pare corregir retorna también las palabras que se han repetido hasta x veces donde x
#es el threshold. Es decir, dice que con más de 10, pero si le pasas threshold 10 te retorna
#con 10 o más (10 incluído) en contradicción con la documentación de get_more_often_user_words
#Esto hay que corregirlo. También en el segundo mensaje te dice con más de 10 y le pasa threshold
#5. Hay unas cuántas cosas que cambiar

print(get_more_often_used_words(freqs))
print("\n")
print("Palabras más frecuentes con más de 5 apariciones.") #Aquí pasa algo raro, porque a parte de
#lo de decir con más de 10 cuando deberían ser 5, también nos encontramos que elide todas las que pasan
#de 10 que ha sacado por pantalla previamente, como si la lista que le hubieramos pasado en el primer
#get_more_often_user_words (no deberia ser used?) las hubiera eliminado
#debe ser por no tener cuidado trabajando con mutables. He cambiado ya lo de 10 por 5 en este print
print(get_more_often_used_words(freqs, threshold=5))

