#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

#-----------------------------------------------------------#

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

user_number = int(input("Ingrese un número entero: ")) 
user_number = len(str(user_number))
print("El número tiene", user_number, "cifras.")

#-----------------------------------------------------------#

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores

primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))

maximo = max(primer_numero, segundo_numero)
minimo = min(primer_numero, segundo_numero) + 1 
suma = 0
for i in range(minimo, maximo):
    suma += i
print("La suma de los números entre", primer_numero, "y", segundo_numero, "es:", suma)

#-----------------------------------------------------------#

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

user = int(input("Ingrese un número: "))
suma = 0
if user == 0:
    print("El número es negativo.")
else:
    while user > 0 :
        suma += user 
        user = int(input("Ingrese otro número (ingrese 0 para FINALIZAR): "))      
#-----------------------------------------------------------#

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

Numero_Alatorio = random.randint(0, 9)
intentos = 0
max_intentos = 9
intentos = 0
max_intentos = 9

for i in range(max_intentos):
    user = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    
    if user == Numero_Alatorio:
        print(f"¡Felicitaciones! ¡Has adivinado el número! Lo adivinaste en {intentos} intentos.")
        break
else:  
    print("Lo siento, has agotado los intentos. El número era:", Numero_Alatorio)

#-----------------------------------------------------------#
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range (100,-1,-2):
        print(i)

#-----------------------------------------------------------#

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

n = int(input("Ingrese un número entero : "))
suma = 0

for i in range(n + 1):
    suma += i 
print("La suma de los números del 0 al", n, "es:", suma)

#----------------------------------------------------------#

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).


contador_positivos = 0
contador_negativos = 0
contador_pares = 0
contador_impares = 0

for i in range (100):
    user = int(input("Ingrese un número: "))
    if user > 0:
        contador_positivos += 1
    elif user < 0:
        contador_negativos += 1
    if user % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
print("Cantidad de números positivos:", contador_positivos)
print("Cantidad de números negativos:", contador_negativos)
print("Cantidad de números pares:", contador_pares)
print("Cantidad de números impares:", contador_impares)

#-----------------------------------------------------------#

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor)

suma = 0
for i in range(3):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / 3
print("La media de los números es:", media)

#-----------------------------------------------------------#
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

numero = input("Ingrese un número: ")
numero_invertido = numero[::-1]  
print("Número invertido:", numero_invertido)
