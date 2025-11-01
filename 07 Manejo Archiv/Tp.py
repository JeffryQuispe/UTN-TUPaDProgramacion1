# Nombre del archivo donde se guardarán los productos
FILENAME = "productos.txt"


# -----------------------------
# 1. Crear archivo inicial con productos (si no existe)
# -----------------------------
def crear_archivo_inicial():
    """Crea el archivo productos.txt con datos iniciales si no existe,
    utilizando manejo de excepciones en lugar del módulo os."""

    archivo_existe = False

    # Intenta abrir el archivo en modo lectura ('r').
    # Si tiene éxito, el archivo existe.
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            # Si la apertura tiene éxito, no hacemos nada más.
            archivo_existe = True
        print(f"Archivo '{FILENAME}' ya existe — se usará su contenido.")

    # Si la apertura falla con FileNotFoundError, el archivo no existe.
    except FileNotFoundError:
        archivo_existe = False
    except Exception as e:
        print(f"Error inesperado al verificar el archivo: {e}")
        return  # Salir si hay otro error grave

    # Si el archivo NO existe, lo creamos.
    if not archivo_existe:
        try:
            # Modo 'w' para escribir y crear el archivo
            with open(FILENAME, "w", encoding="utf-8") as f:
                f.write("Lapicera,120.5,30\n")
                f.write("Cuaderno,250.0,50\n")
                f.write("Resaltador,85.75,40\n")
            print(f"Archivo '{FILENAME}' creado con 3 productos iniciales.")
        except Exception as e:
            print(f"Error al crear el archivo inicial: {e}")


# -----------------------------
# 2 y 4. Leer, mostrar y cargar productos en lista de diccionarios
# -----------------------------
def leer_productos():
    """Lee el archivo, procesa cada línea y carga los datos en una lista de diccionarios."""
    productos = []
    try:
        # Modo 'r' para lectura
        with open(FILENAME, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()  # Limpiar espacios y saltos de línea
                if not linea:
                    continue  # Saltar líneas vacías

                partes = linea.split(",")

                # Validar que tengamos las 3 partes esperadas
                if len(partes) == 3:
                    nombre = partes[0].strip()

                    # Usar try-except para manejar errores de conversión (precio y cantidad)
                    try:
                        precio = float(partes[1])
                    except ValueError:
                        print(f"Advertencia: Precio inválido para {nombre}. Usando 0.0.")
                        precio = 0.0

                    try:
                        cantidad = int(partes[2])
                    except ValueError:
                        print(f"Advertencia: Cantidad inválida para {nombre}. Usando 0.")
                        cantidad = 0

                    # Agregar a la lista como un diccionario
                    productos.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

    except FileNotFoundError:
        # Este error es esperado si el archivo nunca fue creado.
        print("El archivo aún no existe o está vacío.")

    return productos


def mostrar_productos(productos):
    """Muestra los productos cargados en el formato solicitado."""
    print("\n--- Lista de Productos en Memoria ---")
    if not productos:
        print("No hay productos para mostrar.")
    for p in productos:
        # Formato de salida solicitado
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']:.2f} | Cantidad: {p['cantidad']}")
    print("-------------------------------------\n")


# -----------------------------
# 3. Agregar productos desde teclado
# -----------------------------
def pedir_nuevo_producto():
    """Pide al usuario los datos del nuevo producto con validación."""
    print("\n--- Ingreso de Nuevo Producto ---")
    nombre = input("Ingresá el nombre del producto (Enter vacío para cancelar): ").strip()
    if not nombre:
        return None

    # Bucle para validar el precio
    while True:
        try:
            precio_str = input("Ingresá el precio: ").strip()
            precio = float(precio_str)
            if precio < 0:
                print("El precio debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresá un número para el precio.")

    # Bucle para validar la cantidad
    while True:
        try:
            cantidad_str = input("Ingresá la cantidad: ").strip()
            cantidad = int(cantidad_str)
            if cantidad < 0:
                print("La cantidad debe ser un número entero positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresá un número entero para la cantidad.")

    return {"nombre": nombre, "precio": precio, "cantidad": cantidad}


# -----------------------------
# 5. Buscar producto por nombre
# -----------------------------
def buscar_producto(productos, nombre_buscar):
    """Busca un producto por nombre (ignora mayúsculas/minúsculas)."""
    nombre_buscar = nombre_buscar.lower().strip()
    for p in productos:
        if p["nombre"].lower().strip() == nombre_buscar:
            return p
    return None


# -----------------------------
# 6. Guardar todos los productos (sobrescribir archivo)
# -----------------------------
def guardar_productos_actualizados(productos):
    """Sobrescribe el archivo completo con el contenido actual de la lista (Modo 'w')."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            for p in productos:
                # Escribimos los productos actualizados
                f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
        print(f"\nArchivo '{FILENAME}' sobrescrito y actualizado correctamente con {len(productos)} productos.")
    except Exception as e:
        print(f"Error al guardar los productos: {e}")


# -----------------------------
# Programa principal con Menú
# -----------------------------
def main():
    print("=== Gestor de Productos: Persistencia de Datos ===\n")

    # 1. Crear archivo inicial si no existe
    crear_archivo_inicial()

    # 2 y 4. Leer y cargar productos en memoria
    productos = leer_productos()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Mostrar todos los productos")
        print("2. Agregar nuevo producto")
        print("3. Buscar producto por nombre")
        print("4. Guardar cambios y Salir")

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == '1':
            # 2. Mostrar productos
            mostrar_productos(productos)

        elif opcion == '2':
            # 3. Agregar nuevos productos
            nuevo = pedir_nuevo_producto()
            if nuevo is not None:
                productos.append(nuevo)
                print(f"\n¡Producto '{nuevo['nombre']}' agregado a la lista en memoria!")
                print("Recuerda usar la opción 4 para guardar los cambios de forma persistente.")

        elif opcion == '3':
            # 5. Buscar producto
            buscar = input("Ingresá el nombre del producto a buscar: ").strip()
            if buscar:
                resultado = buscar_producto(productos, buscar)
                if resultado:
                    print("\n--- Producto encontrado ---")
                    print(f"Nombre: {resultado['nombre']}")
                    print(f"Precio: ${resultado['precio']:.2f}")
                    print(f"Cantidad: {resultado['cantidad']}")
                    print("---------------------------\n")
                else:
                    print(f"\nEl producto '{buscar}' no existe en la lista.\n")

        elif opcion == '4':
            # 6. Guardar productos actualizados (Sobrescribe todo el archivo) y salir
            guardar_productos_actualizados(productos)
            print("Saliendo del programa. ¡Hasta pronto!")
            break

        else:
            print("\nOpción no válida. Por favor, elegí un número del 1 al 4.")


if __name__ == "__main__":
    main()
