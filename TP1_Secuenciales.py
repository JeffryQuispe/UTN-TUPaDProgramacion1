#1)Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")

#2)Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
nombre = input("ingrese su nombre: ")
print(f"Holo como estas,{nombre}")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = int(input("ingrese su edad: "))
lugar = input("ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
pi  = 3.14
radio = float(input("Ingrese el radio del círculo: "))
perimetro = 2 * pi * radio
area = pi * radio** 2
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")  

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
numero = int(input("Ingrese un número: "))
for i in range(1, 11): 
    tabla = i * numero
    print(f"{numero} x {i} = {tabla}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
user = int(input("Ingrese un número: "))
user2 = int(input("Ingrese otro número: "))
if user and user2 !=0:
    suma = user + user2
    resta = user - user2
    multiplicacion = user * user2
    divicion = user / user2
    print(f"Resultados suma:{suma}, resta: {resta}, multiplicación: {multiplicacion}, división: {divicion}")
else:
    print("Los números deben ser distintos de 0.")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
peso_user = float(input("Ingrese su peso en kg: "))
altura_user = float(input("Ingrese su altura en metros: "))
imc = peso_user / (altura_user ** 2)
print(f"Su índice de masa corporal es: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
temp_user = float(input("ingrese una temperaatura C°: "))
calculo_f = (temp_user * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {calculo_f}°F")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
user_num1 = float(input("Ingrese el primer número: "))
user_num2 = float(input("Ingrese el segundo número: "))
user_num3 = float(input("Ingrese el tercer número: "))
promedio = (user_num1 + user_num2 + user_num3) / 3
print(f"El promedio de los números ingresados es: {promedio}")