# Ingreso de valores
var1 = float(input('Ingrese el primer valor: '))
var2 = float(input('Ingrese el segundo valor: '))

while True:
    
    opcion = input(''' 
            MENU
1. Suma
2. Resta
3. Multiplicación
4. Salir
Elija una opción:              
               ''')

    if opcion == '1':
        resultado = var1 + var2
        print(f"La suma es: {resultado}")

    elif opcion == '2':
        resultado = var1 - var2
        print(f"La resta es: {resultado}")

    elif opcion == '3':
        resultado = var1 * var2
        print(f"La multiplicación es: {resultado}")

    elif opcion == '4':
         print(f"CHAU")
         break
    else:
        print("Opción no válida.")