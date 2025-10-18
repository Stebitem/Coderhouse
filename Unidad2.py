
lista_1 = [10, 20, 30]
lista_2 = ["A", "B", "C"]

print("Lista 1 inicial:", lista_1)
print("Lista 2 inicial:", lista_2)


lista_1.append(456789)
lista_1.append("Hola Mundo")
print("Lista 1 después de añadir elementos:", lista_1)


lista_2.append("Hola y adiós")
lista_2.append(5555)
print("Lista 2 después de añadir elementos:", lista_2)


lista_3 = lista_1[:-1]
print("Lista 3 (lista_1 sin el último):", lista_3)


lista_4 = lista_2[1:-1]
print("Lista 4 (lista_2 sin primero y último):", lista_4)


lista_5 = lista_4 + lista_3
print("Lista 5 (lista_4 + lista_3):", lista_5)