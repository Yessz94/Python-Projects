inventario = {}

def agregar_producto():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    inventario[nombre] = cantidad

def mostrar_inventario():
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad}")

def actualizar_producto():
    nombre = input("Producto a actualizar: ")
    if nombre in inventario:
        cantidad = int(input("Nueva cantidad: "))
        inventario[nombre] = cantidad
    else:
        print("Producto no existe")

def eliminar_producto():
    nombre = input("Producto a eliminar: ")
    inventario.pop(nombre, None)

while True:
    print("\n1. Agregar\n2. Mostrar\n3. Actualizar\n4. Eliminar\n5. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        break
