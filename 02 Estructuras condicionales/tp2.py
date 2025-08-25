#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
user_age = int(input("ingrese su edad: "))
if user_age >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
#---------------------------------------------------------------#

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

user_note = float(input("ingrese su nota: "))
if user_note >= 6 and user_note <= 10:
    print("Aprobado")
else:
    print("Desaprobado")

#---------------------------------------------------------------#

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

user_number = int(input("ingrese un numero par: "))
if user_number % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#---------------------------------------------------------------#

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

user_age2 = int(input("ingrese su edad: "))
if user_age2 < 12:
    print("Niño/a")
elif user_age2 >= 12 and user_age2 < 18:
    print("Adolescente")
elif user_age2 >= 18 and user_age2 < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#---------------------------------------------------------------#
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.
passwored = len(input("ingrese una contraseña (entre 8 y 14 caracteres): "))
if passwored >= 8 and passwored <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#---------------------------------------------------------------#
import random
from statistics import mean, median, mode

numeros_alaoratorios = [random.randint(1, 100) for i in range(50)]
print(numeros_alaoratorios)

calculo_mean = mean(numeros_alaoratorios)
calculo_median = median(numeros_alaoratorios)
calculo_mode = mode(numeros_alaoratorios)
print("Media:", calculo_mean)
print("Mediana:", calculo_median)
print("Moda:", calculo_mode)

if calculo_mean > calculo_median and calculo_mean > calculo_mode:
    print("La media es mayor")
elif calculo_median > calculo_mean and calculo_median > calculo_mode:
    print("La mediana es mayor")
elif calculo_mode > calculo_mean and calculo_mode > calculo_median:
    print("La moda es mayor")
else:
    print("Hay valores iguales entre media, mediana y moda")

#---------------------------------------------------------------#
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
user_string = input("ingrese una frase o palabra: ")
if user_string[-1].lower() in "aeiou":
    user_string += "!"
    print(user_string)

#---------------------------------------------------------------#
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

user_nombre = input("ingrese su nombre: ")
user_option = int(input("ingrese 1 para mayusculas, 2 para minusculas, 3 para primera letra mayuscula: "))
if user_option == 1:
    print(user_nombre.upper())
elif user_option == 2:
    print(user_nombre.lower())
elif user_option == 3:
    print(user_nombre.title())

#---------------------------------------------------------------#
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

user_terremoto = float(input("ingrese la magnitud del terremoto: "))
if user_terremoto < 3:
    print("Muy leve (imperceptible)")
elif user_terremoto >= 3 and user_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif user_terremoto >= 4 and user_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif user_terremoto >= 5 and user_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif user_terremoto >= 6 and user_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#---------------------------------------------------------------#

user_estacion = input("N/S: ").lower()
user_mes = input("Desde el mes (Diciembre , Marzo , Junio , Septiembre): ").lower()
user_dia = int(input("dede el dia (1-31): "))
user_mes2 = input("Hasta el mes (Diciembre , Marzo , Junio , Septiembre): ").lower()
user_dia2 = int(input("Hasta el dia (1-31): "))

if user_estacion == "n":
    if (user_mes == "diciembre" and user_dia == 21) or (user_mes2 == "marzo" and user_dia2 == 20):
        print("Invierno")
    elif (user_mes == "marzo" and user_dia == 21) or (user_mes2 == "junio" and user_dia2 == 20):
        print("Primavera")
    elif (user_mes == "junio" and user_dia == 21) or (user_mes2 == "septiembre" and user_dia2 == 20):
        print("Verano")
    elif (user_mes == "septiembre" and user_dia == 21) or (user_mes2 == "diciembre" and user_dia2 == 20):
        print("Otoño")
    else:
        print("Meses no valido")

elif user_estacion == "s":
    if (user_mes == "diciembre" and user_dia == 21) or (user_mes2 == "marzo" and user_dia2 == 20):
        print("Verano")
    elif (user_mes == "marzo" and user_dia == 21) or (user_mes2 == "junio" and user_dia2 == 20):
        print("Otoño")
    elif (user_mes == "junio" and user_dia == 21) or (user_mes2 == "septiembre" and user_dia2 == 20):
        print("Invierno")
    elif (user_mes == "septiembre" and user_dia == 21) or (user_mes2 == "diciembre" and user_dia2 == 20):
        print("Primavera")
    else:
        print("Meses no valido")
else:
    print("Error")