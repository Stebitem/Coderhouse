colores = {"Rojo", "Blanco", "Azul"}
print("Conjunto inicial:", colores)

colores.add("Violeta")
colores.add("Dorado")
print("Conjunto después de agregar Violeta y Dorado:", colores)

colores.discard("Celeste")   
colores.discard("Blanco")
colores.discard("Dorado")
print("Conjunto después de eliminar Celeste, Blanco y Dorado:", colores)

#Si usamos discard("Celeste") y el elemento no existe en el conjunto, no pasa nada (no da error).
#Si hubiéramos usado remove("Celeste"), sí daría un error (KeyError) porque el color no está en el set.