cantidad_de_partidos = 20
partidos_ganados = int(input("Ingresa los partidos ganados: "))
partidos_pardidos = int(input("Ingresa los partidos perdidos: "))
partidos_empatados = int(input("Ingresa los partidos empatados: "))

resultado = ((partidos_empatados*1) + (partidos_ganados*3) + (partidos_pardidos*0))/cantidad_de_partidos

print(resultado)