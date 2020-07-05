
# coding: utf-8

# Crear una clase `Fraccion` que implemente la representación de un número como una fracción (i.e. numerador/denominador).
# 
# Debe implementar los siguientes métodos:
# * Suma
# * Resta
# * Multiplicación
# * Inversa
# * Imprimir su representación
# * Extra: Posibilidad de convertir el objeto a flotante.

# In[7]:


import math #tiene una función llamada modf que supone la forma más sencilla de obtener la parte decimal con la función modf
import reduce #fichero creado por @LuisMoro que pasa una fracción a su forma irreducible

class Fraccion(object):
    """Clase que implemente la representación de un número decimal finito como una fraccion.
    Se crea el objeto con el argumento que es el número en su expresión decimal. En el propio método init
    se expresa como una fracción irreducible"""
    def __init__(self, decimal): 
        """Inicializa el número con valor decimal"""
        self.decimal = decimal
        
#Esto no hace falta pues ya lo tengo en el modulo que he creado, llamado "reduce"
#No tiene sentido guardar en una clase del objeto algo tan general para tener que llamarlo luego desde las demás
#Soy consciente de que se puede hacer de otras formas pero esta era con la que más claro me parecia el resultado
#    def fraccion_irreducible(self):
#       """Calcula la fracción irreducible del decimal finito aportado"""
#       numerador = self.decimal 
#       denominador = 1
#       while math.modf(numerador)[0] != 0: #modf toma la parte decimal del numerador, que multiplicaré por 10 hasta que sea un entero
#           numerador = numerador*10
#           denominador = denominador*10
#       numerador = int(numerador) #he hecho el while a un número con parte decimal, ahora es un entero
#       #y yo quiero que no salgan coma y ceros
    
        #En este momento tengo ya el número expresado como fracción, pero no como fracción irreducible, vamos a ello
        #Lo he creado en otro fichero a parte por ser un aspecto más general y queda poco intuituvo mostrarlo como una función más
        #de la clase fracción. Por eso está guardado en el fichero reduce.py como metodo reductor(num,denom)
#       numerador,denominador = reduce.reductor(numerador,denominador)
#       return numerador,denominador
    
    def multiplicacion(self,other):
        """Realiza el producto de dos objetos de la clase fraccion, que son numeros decimales finitos
        y retorna su producto en forma de fraccion irreducible. También sería posible modificarlo para que se le pasen
        dos objetos en forma decimal, use la clase que los convierte a fraccion (ahora esta en un modulo a parte
        para llamarla pero se puede implementar como clase), hacer el producto de numeradores y denominadores
        y luego pasarlo a fraccion irreducbile. De esta forma hariamos el producto propiamente mientras estan
        representados como fracciones. Aqui los multiplicamos como decimales y luego ya lo pasamos a fraccion irrreducible 
        el resultado, simplemente porque parece más elegante """
        producto_decimal = self.decimal*other.decimal
        #CUIDADO, pues el producto de ambos puede dar lugar a un numero decimal no finito...igual es mejor operar con fracciones y luego reducir
        return reduce.reductor(producto_decimal)
            


# In[8]:


prueba = Fraccion(2.4584)


# In[9]:


prueba2 = Fraccion(3.24)


# In[ ]:


prueba.multiplicacion(prueba2) #por ejemplo, en este caso, si pasaramos prueba y prueba 2 a fraccion, hicieramos
#el producto de las fracciones y buscaramos su fraccion irreducible todo queda bien. Pero si haces el producto
#con las expresiones decimales, te quedan un decimal no finito como resultado. Por consiguiente cuando llamas al
#reduce.reductor(decimal) dentro del atributo "multiplicacion", cuando se hace el primer paso de reductor,
# y trata de pasar a fraccion el decimal, lo primero que intenta es quitarse todos los digitos a la derecha de la
#coma del decimal(que pasa a ser el numerador) multiplicando numerador y denominador por 10
# luego si hay infinitos digitos entra en un bucle interminable. Si haces ese producto con python a pelo 
#ves que te lo redondea, pero yo no se hacer eso de momento. 


# In[11]:




