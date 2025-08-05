#formas de controlar while
"""
Identificadores o tipos de datos primitivos por nuevos sean reales o enteros 
por cadenas de texto 
no primitivos listas, diccionarios, tuplas, conjuntos, sets
rangos, arreglos, matrices.
"""
#Rango control letra 
print("Programa en clase")
palabra = input("Diga una letra:")
while palabra.lower() =="s":
    palabra = input("Diga una letra:")
print("Fin del programa")

#Algoritmo que simula un ciclo repita hasta que la condicion se cumpla, algoritmo propio
print("Programa propio")
palabra = input("Diga una letra:")
while palabra.lower() !="s":
    palabra = input("Diga una letra:")
print("Fin del programa")

contador = 0
while True:
    if contador == 10:
        contador += 1
        print(contador)
        break
    else:
        print("El ciclo ha terminado")