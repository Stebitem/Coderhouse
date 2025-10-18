texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

frases = texto.split("&")

frases_limpias = []
for f in frases:
    f = f.strip()
    f = f.capitalize()
    if not f.endswith("."):
        f += "."
    frases_limpias.append(f)

resultado = "\n\n".join(frases_limpias)

print(resultado)
