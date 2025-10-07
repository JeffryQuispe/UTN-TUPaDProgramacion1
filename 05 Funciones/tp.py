# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo(saludo):
    return saludo
print(imprimir_hola_mundo('Hola Mundo!'))


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"
name = input("Ingresa tu nombre: ")
print(saludar_usuario(name))


# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima:
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre,apellido,edad,residencia):
    return f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}"
name = input("Ingresa tu nombre: ")
surname = input("Ingresa tu apellido: ")
age = int(input("Ingresa tu edad: "))
residence = input("Ingresa tu residencia: ")
print(informacion_personal(name,surname,age,residence))


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return 3.14 * radio * radio
def calcular_perimeter_circulo(radio):
    return 2 * 3.14 * radio
radio = float(input("Ingresa radio: "))
print(f"El area es {calcular_area_circulo(radio)} cm")
print(f"El perimetro es {calcular_perimeter_circulo(radio)} cm")


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600
segundos = int(input("Ingresa segundos: "))
print(f"{segundos} segundos equivale a {segundos_a_horas(segundos):.2f} horas")


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicacion(numero):
    for i in range(0,11):
        print(f" {i} * {numero} = {i * numero}")
numero = int(input("Ingresa un numero: "))
tabla_multiplicacion(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)
nun1 = float(input("Ingresa un Primer numero: "))
nun2 = float(input("Ingresa un Segundo numero: "))

print(f"Los numero para la operiones es {nun1} y {nun2}")
print(f"Suma es {operaciones_basicas(nun1,nun2)[0]}")
print(f"Resta es {operaciones_basicas(nun1,nun2)[1]}")
print(f"Multiplicación  es {operaciones_basicas(nun1,nun2)[2]}")
print(f"Divición es {operaciones_basicas(nun1,nun2)[3]}")


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

def calcular_imc(peso,altura):
    return peso / (altura**2)
peso = float(input("Ingresa un peso: "))
altura = float(input("Ingresa un altura: "))
print(f"El imc es {calcular_imc(peso,altura):.2f}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
celsius = float(input("Ingresa un celsius: "))
print(f"En fahrenheit es {celsius_a_fahrenheit(celsius):.2f}")

# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calculadora_promedio(a,b,c):
    return (a + b + c) / 3
a = float(input("Ingresa un Primer numero: "))
b = float(input("Ingresa un Segundo numero: "))
c = float(input("Ingresa un Tercer numero: "))
print(f"El promedio es {calculadora_promedio(a, b, c):.2f}")