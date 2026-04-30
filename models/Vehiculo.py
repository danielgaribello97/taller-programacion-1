class Vehiculo:
    """Clase padre que define atributos comunes para todos los vehículos."""
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self):
        """Método base para ser sobrescrito."""
        self.velocidad += 10
        print(f"El vehículo {self.marca} está acelerando. Velocidad base: {self.velocidad} km/h")