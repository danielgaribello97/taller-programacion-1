from models.Vehiculo import Vehiculo

class Coche(Vehiculo): # Ahora hereda de Vehiculo[cite: 11]
    """
    Clase para la gestión de vehículos tipo coche.
    Hereda de Vehiculo y utiliza composición con Motor[cite: 8, 9, 11].
    """

    def __init__(self, marca, modelo, anio, motor):
        # Inicialización en la clase padre[cite: 11]
        super().__init__(marca, modelo)
        
        # Atributos específicos con validación
        self.set_marca(marca)
        self.set_modelo(modelo)
        self.set_anio(anio)
        self.__motor = motor 

    def set_marca(self, marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo

    def set_anio(self, anio):
        if 1886 <= anio <= 2026:
            self.__anio = anio
        else:
            self.__anio = 0
            print(f"Error: El año {anio} está fuera de los rangos permitidos.")

    def get_anio(self):
        return self.__anio

    def describir(self):
        print(f"Vehículo: {self.__marca} {self.__modelo} | Modelo: {self.__anio}")
        print(f"Especificaciones: {self.__motor.obtener_info_motor()}")
        
    def acelerar(self):
        """Sobrescritura del método acelerar usando el motor (Ejercicio 5)[cite: 11]."""
        try:            
            self.velocidad = self.__motor.incrementar_velocidad()
            print(f"La velocidad (Coche) incrementa a: {self.velocidad}")
        except ValueError as error:
            print(f"Error en motor: {error}")