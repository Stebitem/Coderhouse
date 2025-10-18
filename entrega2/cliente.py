class Cliente:
    cantidad_clientes = 0

    def __init__(self, nombre, correo, direccion, saldo=0):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.saldo = saldo
        Cliente.cantidad_clientes += 1

    def __str__(self):
        return f"Cliente: {self.nombre} - Correo: {self.correo}"
    def agregar_saldo(self, monto):
        """Agrega dinero al saldo del cliente"""
        if monto > 0:
            self.saldo += monto
            print(f"Se agregaron ${monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("El monto debe ser positivo.")
    def realizar_compra(self, valor):
        """Resta dinero del saldo si alcanza para la compra"""
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Compra realizada por ${valor}. Saldo restante: ${self.saldo}")
        else:
            print("Saldo insuficiente para realizar la compra.")
