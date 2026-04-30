from models.Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    """Clase hija que representa el ejercicio 4 y 5[cite: 11]."""
    
    def __init__(self, marca, modelo, tipo="Montaña"):
        # Inicializa marca y modelo en la clase padre[cite: 11]
        super().__init__(marca, modelo)
        self.tipo = tipo

    def acelerar(self):
        # Sobrescritura: La bicicleta aumenta de 2 en 2[cite: 11]
        self.velocidad += 2
        print(f"Pedaleando la bicicleta {self.tipo} {self.marca}. Velocidad: {self.velocidad} km/h")