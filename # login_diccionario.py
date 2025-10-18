usuarios = {
}
def login():
    global usuarios
    print("\n=== LOGIN ===")
    user = input("Ingrese usuario: ").strip()
    pw = input("Ingrese contraseña: ").strip()

    if user in usuarios and usuarios[user] == pw:
        print(f"Bienvenido {user}, login exitoso.")
    else:
        print("Usuario o contraseña incorrectos.")

def mostrar():
    global usuarios
    print("\n=== MOSTRAR USUARIOS ===")
    print("1) Listar todos los usuarios")
    print("2) Buscar usuarios que contengan ciertos caracteres")

    opcion = input("Elija opción: ").strip()

    if opcion == "1":
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados:")
            for u in usuarios:
                print(f"- {u}")
    elif opcion == "2":
        criterio = input("Ingrese parte del nombre a buscar: ").strip()
        encontrados = [u for u in usuarios if criterio in u]

        if encontrados:
            print("Usuarios encontrados:")
            for u in encontrados:
                print(f"- {u}")
        else:
            print("No se encontraron usuarios con ese criterio.")
    else:
        print("Opción inválida.")

def guardar():
    global usuarios
    print("\n=== REGISTRAR USUARIO ===")
    user = input("Ingrese nuevo usuario: ").strip()

    if user in usuarios:
        print("El usuario ya existe.")
        return

    pw = input("Ingrese contraseña: ").strip()
    usuarios[user] = pw
    print(f"Usuario '{user}' registrado con éxito.")

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1) Login")
    print("2) Mostrar usuarios")
    print("3) Guardar usuario")
    print("4) Salir")

    opcion = input("Seleccione una opción: ").strip()
    if opcion == "1":
        login()
    elif opcion == "2":
        mostrar()
    elif opcion == "3":
        guardar()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida, intente nuevamente.")