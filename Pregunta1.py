"""
1) [20 p.] Formule una función en Python que, dado un número entero positivo (llamémosle m),
genere una lista con todos sus divisores enteros exactos.
Incluya a 1 y a m entre los divisores. Esta función puede serle útil.
"""


def Es_Divisible(m, n):
# m es un entero y corresponde al dividendo
# n es un entero y corresponde al divisor
# Usaremos la propiedad de residuo de una división
# Devolver True si n divide exactamente a m
# Devolver False en caso contrario
    return (m % n == 0)


def Divisores(m):
    n = m//2 #Divide a la mitad el número
    divisores=[]#Lista
    while(n!=0):#Comprueba
        if Es_Divisible(m,n):
            divisores.append(n) #Agregue al final 
        n-=1
    return divisores


