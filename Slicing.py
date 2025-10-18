cadena = "acitametaM ,5.8 ,ordeP otipeP"
cadena_volteada = cadena[::-1]
nombre_alumno = cadena_volteada[:12]
nota = cadena_volteada[14:17]
materia = cadena_volteada[19:]
print(nombre_alumno + " ha sacado un " + nota + " en " + materia)