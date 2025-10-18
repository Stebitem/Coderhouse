from cliente import Cliente

# Lista para guardar los clientes creados
lista_clientes = []
def mostrar_menu():
    print("\n=== MENÚ DE CLIENTES ===")
    print("1. Agregar cliente")
    print("2. Mostrar todos los clientes")
    print("3. Agregar saldo a un cliente")
    print("4. Realizar compra")
    print("5. Mostrar cantidad de clientes creados")
    print("6. Salir")
def buscar_cliente(nombre):
    """Devuelve el cliente si lo encuentra por nombre"""
    for c in lista_clientes:
        if c.nombre.lower() == nombre.lower():
            return c
    return None
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        correo = input("Correo electrónico: ")
        direccion = input("Dirección: ")
        saldo = float(input("Saldo inicial: "))

        nuevo_cliente = Cliente(nombre, correo, direccion, saldo)
        lista_clientes.append(nuevo_cliente)
        print(f"\nCliente '{nombre}' agregado correctamente.")

    elif opcion == "2":
        print("\n=== LISTA DE CLIENTES ===")
        if not lista_clientes:
            print("No hay clientes cargados.")
        else:
            for c in lista_clientes:
                print(f"{c} - Saldo: ${c.saldo}")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del cliente: ")
        cliente = buscar_cliente(nombre)
        if cliente:
            monto = float(input("Monto a agregar: "))
            cliente.agregar_saldo(monto)
        else:
            print("Cliente no encontrado.")
    elif opcion == "4":
        nombre = input("Ingrese el nombre del cliente: ")
        cliente = buscar_cliente(nombre)
        if cliente:
            valor = float(input("Valor de la compra: "))
            cliente.realizar_compra(valor)
        else:
            print("Cliente no encontrado.")
    elif opcion == "5":
        print(f"\nCantidad total de clientes creados: {Cliente.cantidad_clientes}")
    elif opcion == "6":
        print("\nSaliendo del programa...")
        break
    else:
        print("Opción inválida. Intenta nuevamente.")