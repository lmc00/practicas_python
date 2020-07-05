import math
def reductor(decimal):
    """Fichero complementario en el que pasada un decimal finito y devuelve el numerador y denominador 
    de la fracción irreducible que representa ese decimal"""
    numerador = decimal
    denominador = 1
    while math.modf(numerador)[0] != 0: #modf toma la parte decimal del numerador, que multiplicaré           por 10 hasta que sea un entero
        numerador = numerador*10
        denominador = denominador*10
    numerador = int(numerador) 
    contador = 2;
    while contador <= min(numerador,denominador):
        if numerador % contador == 0 and denominador % contador == 0:
            numerador = numerador/contador
            denominador = denominador/contador
        else:
            contador = contador+1
    return numerador,denominador


def irreducible(num, dem):
    """Es exactamente como reductor, solo que se ahorra el primer paso ya que ahora ya le estamos pasando fraccion directamente"""
    cont = 2;
    while cont <= min(num,dem):
        if num % cont == 0 and dem % cont == 0:
            num = num/cont
            dem = dem/cont
        else:
            cont = cont+1
    return num,dem

