# 1) Crea una función recursiva que calcule el factorial de un número.
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial 
# de todos los números enteros entre 1 y el número que indique el usuario.

numero = int(input("Ingrese un número entero positivo: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(numero))

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci 
# en la posición indicada. Posteriormente, muestra la serie completa hasta 
# la posición que el usuario especifique.

numero_fib = int(input("Ingrese la posición de la serie de Fibonacci: "))
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(numero_fib))

# 3) Crea una función recursiva que calcule la potencia de un número base 
# elevado a un exponente, utilizando la fórmula n^m = n * n^(m-1).
# Prueba esta función en un algoritmo general.

numero_base = int(input("Ingrese la base: "))
numero_exponente = int(input("Ingrese el exponente: "))
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
print(potencia(numero_base, numero_exponente))

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero_binario = int(input("Ingrese un número entero positivo para convertir a binario: "))
print(f"El número {numero_binario} en binario es: {decimal_a_binario(numero_binario)}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# - La solución debe ser recursiva.
# - No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra_input = input("Ingrese una palabra para verificar si es palíndromo: ")
print(es_palindromo(palabra_input))


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# - No se puede convertir el número a string.
# - Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)
numero_suma = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
print(suma_digitos(numero_suma))

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
# Ejemplos:
# contar_bloques(1)_

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)
numero_bloques = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
print(contar_bloques(numero_bloques))

# 8) Función recursiva que cuenta cuántas veces aparece un dígito dentro de un número

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
numero_contar = int(input("Ingrese un número entero positivo: "))
digito_contar = int(input("Ingrese un dígito (0-9) para contar en el número: "))
print(contar_digito(numero_contar, digito_contar))