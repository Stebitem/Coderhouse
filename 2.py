matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

# Recorremos la matriz y añadimos el cuarto elemento
for fila in matriz:
    fila.append(sum(fila[:3]))

print(matriz)