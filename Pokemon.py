class Pokemon:
    def __init__(self, nombre="", calidad="", vida=0, daño=0, defensa=0, costo_venta=0):
        self.nombre = nombre
        self.calidad = calidad
        self.vida = vida
        self.daño = daño
        self.defensa = defensa
        self.costo_venta = costo_venta

    def __str__(self):
        return f"{self.nombre} (HP: {self.vida}, ATK: {self.daño}, DEF: {self.defensa}, Valor: ${self.costo_venta})"