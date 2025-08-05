import time 
import os
inicio = time.time()
for i in range (0,101):
    print(i)
fin = time.time()
tiempoFinal = fin - inicio
print(f"Tiempo de ejecución de for: {tiempoFinal:.6f}  segundos")
time.sleep(5)# Pausa de 5 segundos
os.system('cls')# Limpiar la consola

inicio = time.time()
contador = 0
while contador <= 100:
    print(contador)
    contador = contador + 1
fin = time.time()
tiempoFinal = fin - inicio
print(f"Tiempo de ejecución: {tiempoFinal:.6f} segundos")