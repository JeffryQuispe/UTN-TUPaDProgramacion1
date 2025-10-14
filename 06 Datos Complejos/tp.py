# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas={
    "Banana": 1200,
    "Ananá": 2500,
    "Melon": 3000,
    "Uva": 1450
}
print(precios_frutas)
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
print("----- Actualizao -------")
precios_frutas["Banana"]=1330
precios_frutas["Mnazana"]=1700
precios_frutas["Melon"]=2800
print(precios_frutas)


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

lista = list(precios_frutas.keys())
print(type(lista))
print(lista)


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

registo_usuario = int(input("Ingrese Cuanto contacto queres Registrar: "))

nombre = {}

for i in range(registo_usuario):
    Nombre = input("Ingrese el nombre del contacto: ").lower() .strip()
    Telefono = int(input("Ingrese el telefono del contacto: "))

    nombre[Nombre] = Telefono

print(type(nombre))
print(nombre)

consultar = input("Ingrese el nombre del contacto: ").lower() .strip()
if consultar in nombre.keys():
    print(f"El telefono es : {nombre[consultar]}")
else:
    print("El nombre del contacto no existe")


# 5) Solicita al usuario una frase e imprime:
#    • Las palabras únicas (usando un set).
#    • Un diccionario con la cantidad de veces que aparece cada palabra.
#    Ejemplo: (ingreso: "hola mundo hola") -> set: {"hola", "mundo"} y conteo: {"hola": 2, "mundo": 1}

frase = input("Ingresá una frase: ").lower().strip()
palabras = frase.split()

unicas = set(palabras)
conteo = Counter(palabras)

print("Palabras únicas (set):", unicas)
print("Recuento (diccionario):", dict(conteo))

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#    Luego, mostrá el promedio de cada alumno.
#    Ejemplo: Alumno: Ana -> notas (8, 7, 9) -> promedio: 8.0


alumnos = {}

for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ").strip()
    n1 = float(input("  Nota 1: "))
    n2 = float(input("  Nota 2: "))
    n3 = float(input("  Nota 3: "))
    alumnos[nombre] = (n1, n2, n3)

print("\nPromedios:")
for nombre, notas in alumnos.items():
    prom = sum(notas) / len(notas)
    print(f"  {nombre}: {prom:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#    • Mostrá los que aprobaron ambos parciales.         (intersección)
#    • Mostrá los que aprobaron solo uno de los dos.     (diferencia simétrica)
#    • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). (unión)

print("Ingresá los legajos (números) aprobados en cada parcial, separados por comas.")
p1 = set(int(x) for x in input("Parcial 1: ").replace(" ", "").split(",") if x)
p2 = set(int(x) for x in input("Parcial 2: ").replace(" ", "").split(",") if x)

ambos = p1 & p2                      # intersección
solo_uno = p1 ^ p2                   # diferencia simétrica
al_menos_uno = p1 | p2               # unión

print("\nAprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial (sin repetir):", al_menos_uno)


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#    Permití al usuario:
#    • Consultar el stock de un producto ingresado.
#    • Agregar unidades al stock si el producto ya existe.
#    • Agregar un nuevo producto si no existe.
stock = {}  # nombre -> unidades (int)

while True:
    print("""
--- MENÚ STOCK ---
1) Consultar stock de un producto
2) Agregar unidades a un producto existente
3) Agregar nuevo producto
4) Listar todo
5) Salir
""")
    op = input("Opción: ").strip()

    if op == "1":
        prod = input("Producto a consultar: ").strip().lower()
        if prod in stock:
            print(f"Stock de {prod}: {stock[prod]} unidades")
        else:
            print("No existe ese producto.")

    elif op == "2":
        prod = input("Producto existente: ").strip().lower()
        if prod in stock:
            try:
                cant = int(input("Unidades a agregar: "))
                if cant < 0:
                    print("No se aceptan números negativos.")
                else:
                    stock[prod] += cant
                    print(f"Nuevo stock de {prod}: {stock[prod]}")
            except ValueError:
                print("Cantidad inválida.")
        else:
            print("No existe ese producto. Usá la opción 3 para crearlo.")

    elif op == "3":
        prod = input("Nuevo producto: ").strip().lower()
        if prod in stock:
            print("Ya existe ese producto.")
        else:
            try:
                cant = int(input("Stock inicial: "))
                if cant < 0:
                    print("No se aceptan números negativos.")
                else:
                    stock[prod] = cant
                    print(f"Producto '{prod}' agregado con {cant} unidades.")
            except ValueError:
                print("Cantidad inválida.")

    elif op == "4":
        if not stock:
            print("No hay productos cargados.")
        else:
            print("Listado de stock:")
            for k, v in stock.items():
                print(f"  - {k}: {v}")

    elif op == "5":
        print("Saliendo del gestor de stock.")
        break
    else:
        print("Opción inválida.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#    Permití:
#    • Agregar un evento en (día, hora).
#    • Consultar si hay evento en (día, hora).
#    • Listar todos los eventos cargados.
agenda = {}  # (dia, hora) -> evento (str)

while True:
    print("""
--- MENÚ AGENDA ---
1) Agregar evento (día, hora)
2) Consultar evento por (día, hora)
3) Listar todos los eventos
4) Salir
""")
    op = input("Opción: ").strip()

    if op == "1":
        dia = input("Día (ej: Lunes): ").strip().title()
        hora = input("Hora (ej: 14:00): ").strip()
        evento = input("Evento: ").strip()
        clave = (dia, hora)
        if clave in agenda:
            print("Ya hay un evento en ese día y hora. Se reemplazará.")
        agenda[clave] = evento
        print("Evento guardado.")

    elif op == "2":
        dia = input("Día a consultar: ").strip().title()
        hora = input("Hora a consultar: ").strip()
        clave = (dia, hora)
        if clave in agenda:
            print(f"Evento en {dia} {hora}: {agenda[clave]}")
        else:
            print("No hay evento en ese día y hora.")

    elif op == "3":
        if not agenda:
            print("La agenda está vacía.")
        else:
            print("Eventos:")
            # Orden opcional por día y hora
            for (d, h) in sorted(agenda.keys()):
                print(f"  {d} {h} -> {agenda[(d, h)]}")

    elif op == "4":
        print("Saliendo de la agenda.")
        break
    else:
        print("Opción inválida.")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Perú": "Lima"
}

# Invertimos el diccionario: capital → país
capitales = {capital: pais for pais, capital in paises.items()}

print("Diccionario original:")
print(paises)

print("\nDiccionario invertido:")
print(capitales)