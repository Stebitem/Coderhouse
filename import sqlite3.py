import sqlite3
import hashlib

# --- FUNCIONES ---
def crear_tabla():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE,
        contrasena TEXT
    )
    """)
    conexion.commit()
    conexion.close()

def registrar_usuario(usuario, contrasena):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    # Encriptar contraseña con SHA256
    hash_pass = hashlib.sha256(contrasena.encode()).hexdigest()

    try:
        cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, hash_pass))
        conexion.commit()
        print("✅ Usuario registrado correctamente.")
    except sqlite3.IntegrityError:
        print("⚠️ El usuario ya existe.")
    conexion.close()

def login(usuario, contrasena):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    hash_pass = hashlib.sha256(contrasena.encode()).hexdigest()

    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND contrasena=?", (usuario, hash_pass))
    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        print("🔓 Login exitoso. ¡Bienvenido!")
        return True
    else:
        print("❌ Usuario o contraseña incorrectos.")
        return False


# --- PROGRAMA PRINCIPAL ---
crear_tabla()

while True:
    opcion = input("""
    MENU
    1. Registrar usuario
    2. Iniciar sesión
    3. Salir
    Elija una opción: """)

    if opcion == "1":
        user = input("Ingrese un nombre de usuario: ")
        pwd = input("Ingrese una contraseña: ")
        registrar_usuario(user, pwd)

    elif opcion == "2":
        user = input("Usuario: ")
        pwd = input("Contraseña: ")
        login(user, pwd)

    elif opcion == "3":
        print("👋 Saliendo del sistema...")
        break
    else:
        print("Opción no válida.")
