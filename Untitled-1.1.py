class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
   
    def imprimir(self):
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        if self.nota < 5:
            print(f"{self.nombre} desaprobó la materia.")
        else:
            print(f"{self.nombre} aprobó la materia.")

alumno1 = Alumno("Donato", 8)
alumno2 = Alumno("Sofía", 4)

alumno1.imprimir()
alumno1.resultado()

print("----------------------------------")  

alumno2.imprimir()
alumno2.resultado()
