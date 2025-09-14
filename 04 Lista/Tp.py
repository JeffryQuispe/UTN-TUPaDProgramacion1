#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.
nota = [ 10,9,5,7,8,6,10,10,3,10]
print(nota)
nota_alta = max(nota)
print(nota_alta)
nota_bja = min(nota)
print(nota_bja)
calculo = 0
for i in nota:
    calculo += i
promedio = calculo / len(nota)
print(promedio)

#---------------------------------------------------------------------#

#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del métod sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

lista =[]
for producto in range(1,6):
    user = input(f"Introduce el {producto} producto : ")
    lista.append(user)
lista.sort()
print(lista)
eliminar = input("Introduce el producto que desea eliminar: ")
if eliminar in lista:
    lista.remove(eliminar)
    print(lista)
else:
    print("El producto no existe")

#----------------------------------------------------------------#

#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
lista_pares =[]
lista_inpares = []
for numero in range(1,100):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_inpares.append(numero)
print(f"La lista de pares tienen {len(lista_pares)}  numeros")
print(f"La lista de Inpares tienen {len(lista_inpares)}  numeros")
print(lista_pares)
print(lista_inpares)

#--------------------------------------------------------------------------#

#4) Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

lista_repativas = [2,2,2,3,41,2,1,5,2,5,4,2,1,41,10,11,10]
lista_repativas = list(set(lista_repativas))
print(lista_repativas)

#------------------------------------------------------------------#

#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

estudiantes =["pedro","jeffry","javier","aldana","mati","jesus","daniel","adri"]

menu = ("""====== 1 =======
1) Agregar estudiante
2) Eliminar Estudiante""")
print(menu)
print(estudiantes)
user = int(input("Ingrese Numero: "))
if  user == 1:
    print("Agregar estudiante")
    estudiante = input("Introduce el estudiante: ")
    estudiantes.append(estudiante)
    print(estudiantes)
elif user == 2:
    print("Eliminar estudiante")
    estudiante = input("Introduce el estudiante: ")
    estudiantes.remove(estudiante)
    print(estudiantes)
else:
    print("GRACIAS POR VENIR.....")

#-------------------------------------------------------------------------------#

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).
# Lista original con 7 números

numeros = [10, 20, 30, 40, 50, 60, 70]
print("Lista original:", numeros)


ultimo = numeros.pop()
numeros.insert(0, ultimo)

print("Lista rotada:", numeros)

#----------------------------------------------------------------------------------------------#
#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

semana = [
    [15, 25],  # Día 1
    [17, 28],  # Día 2
    [14, 22],  # Día 3
    [13, 20],  # Día 4
    [18, 27],  # Día 5
    [16, 23],  # Día 6
    [19, 30]   # Día 7
]

suma_min = 0
suma_max = 0

for minima, maxima in semana:
    suma_min += minima
    suma_max += maxima

prom_min = suma_min / len(semana)
prom_max = suma_max / len(semana)

print(f"Promedio de mínimas: {prom_min:.2f}°")
print(f"Promedio de máximas: {prom_max:.2f}°")

mayor_amplitud = 0
dia_mayor = 0

for i, (minima, maxima) in enumerate(semana, start=1):
    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor = i

print(f"La mayor amplitud térmica fue de {mayor_amplitud}° el día {dia_mayor}")

#------------------------------------------------------------------------------------#

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.
# Matriz con las notas de 5 estudiantes en 3 materias
# Cada fila = [nota_materia1, nota_materia2, nota_materia3]
notas = [
    [7, 8, 6],
    [5, 9, 10],
    [6, 6, 7],
    [9, 8, 8],
    [10, 7, 9]
]

print("Promedios por estudiante:")
for i, fila in enumerate(notas, start=1):
    promedio = sum(fila) / len(fila)
    print(f"Estudiante {i}: {promedio:.2f}")

print("\nPromedios por materia:")
num_materias = len(notas[0])

for j in range(num_materias):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    promedio = suma / len(notas)
    print(f"Materia {j+1}: {promedio:.2f}")


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

juego = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]


for fila in juego:
    print(" ".join(fila))
print()

user = input("¿Quiere seguir jugando? (s/n): ")

if user.lower() == "s":
    for turno in range(9):  # hasta 9 jugadas posibles
        print(f"Turno {turno+1}")
        fila = int(input("Ingrese la fila (0,1,2): "))
        col = int(input("Ingrese la columna (0,1,2): "))
        simbolo = input("Ingrese X u O: ").upper()

        # Actualizar el tablero
        juego[fila][col] = simbolo

        # Mostrar tablero después de la jugada
        for f in juego:
            print(" ".join(f))
        print()

#--------------------------------------------------------------------------------#
#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [2, 4, 9, 10, 5, 3, 1],    # Producto 1
    [3, 5, 12, 15, 9, 18, 7],  # Producto 2
    [4, 6, 16, 18, 1, 92, 0],  # Producto 3
    [4, 2, 41, 21, 3, 91, 2]   # Producto 4
]


print("Totales por producto:")
totales_productos = []
for i, fila in enumerate(ventas, start=1):
    total = sum(fila)
    totales_productos.append(total)
    print(f"Producto {i}: {total}")


print("\nVentas totales por día:")
dias = len(ventas[0])
totales_dias = []
for j in range(dias):
    suma_dia = sum(ventas[i][j] for i in range(len(ventas)))
    totales_dias.append(suma_dia)
    print(f"Día {j+1}: {suma_dia}")

dia_max = max(range(dias), key=lambda j: totales_dias[j])
print(f"\nEl día con más ventas fue el día {dia_max+1} con {totales_dias[dia_max]} ventas")


prod_max = max(range(len(ventas)), key=lambda i: totales_productos[i])
print(f"El producto más vendido fue el producto {prod_max+1} con {totales_productos[prod_max]} ventas")
