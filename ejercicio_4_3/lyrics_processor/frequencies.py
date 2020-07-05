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