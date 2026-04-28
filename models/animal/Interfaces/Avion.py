from models.animal.Interfaces.Volador import Volador

class Avion(Volador):
    def volar(self):
        print("El avión activa sus turbinas y despega de la pista.")
