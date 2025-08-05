
"""
Float numero = 3.14
doble numero = 3.1489
"""
#enteros int
#booleanos bool 
#string
"""
tipos de condicionales 
if
elif
else
casos -> match apartir de la version 3.10
ojo con las versiones de python, por que las versiones inferiores no son compatibles con alguna sintaxis de versiones superiores

ciclo ciclicos => ciclos de repeticion 
for = para 
while = mientras 
break = romper # palabras reservadas 
continue = continuar #palabras reservadas en python 
pass = no hacer nada  

"""

#Condional simple 
print("---------------------- ejemplo condicional simple ----------------------")
if True:
    print("Oe parchese")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Condicionales anidados
print("---------------------- ejemplo condicionales anidados ----------------------")
print("Segun el numero es el rol que te va a mostrar")
opc = int(input("Digite el numero:"))
if opc == 1:
    print("Opcion 1 administrador") 
elif opc == 2:
    print("Opcion 2 usuario")
elif opc == 3:
    print("Opcion 3 aprendiz")
else:
    print("Opcion no valida")

#Condicionales con match (Python 3.10+)
#Es una forma de hacer condicionales mas limpias y ordenadas
print("---------------------- ejemplo condionales con match ----------------------")
print("Segun el numero es el rol que te va a mostrar")
opci = int(input("Digite el numero:"))
match opci:
    case 1:
        print("Opcion 1 administrador")
    case 2:
        print("Opcion 2 usuario")
    case 3:
        print("Opcion 3 aprendiz")
    case _:
        print("Opcion no valida")

#Ciclo for recorrido ascendente
print("---------------------- ejemplo ascendente ----------------------")
for i in range(1, 11):
    print(i)

#Ciclo for recorrido descendente
print("---------------------- ejemplo descendente ----------------------")
for i in range(10, 0, -1): 
    print(i)

#Ciclo for recorrido en intervalo de 2 en 2
print("---------------------- ejemplo intervalo de 2 en 2 de menor a mayor----------------------")
for i in range(1, 11, 2): 
    print(i)

#ciclo for recorrido en intervalo de 2 en 2 descendente
print("---------------------- ejemplo intervalo de 2 en 2 de mayor a menor ----------------------")
for i in range(11, 1, -2): 
    print(i)  

print("---------------------- ejemplo variable ----------------------")
Variable = "Hola mundo"
