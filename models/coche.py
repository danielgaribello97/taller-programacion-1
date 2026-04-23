class Coche:
    """
    Clase base para la gestión de vehículos tipo coche.
    Implementa validaciones de integridad y composición con la clase Motor.
    """

    def __init__(self, marca, modelo, anio, motor):
        # Inicialización de atributos a través de setters para asegurar validación
        self.set_marca(marca)
        self.set_modelo(modelo)
        self.set_anio(anio)
        # Se establece la relación de composición con un objeto Motor
        self.__motor = motor 

    # --- Métodos de Control de Acceso (Encapsulamiento) ---
    # Se utilizan métodos públicos para gestionar atributos privados

    def set_marca(self, marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo

    def set_anio(self, anio):
        # Validación: Solo se permiten años desde la creación del primer auto
        if 1886 <= anio <= 2026:
            self.__anio = anio
        else:
            self.__anio = 0
            print(f"Error: El año {anio} está fuera de los rangos permitidos.")

    def get_anio(self):
        return self.__anio

    # --- Métodos de Representación ---

    def describir(self):
        """Imprime el estado actual del vehículo incluyendo su motorización."""
        print(f"Vehículo: {self.__marca} {self.__modelo} | Modelo: {self.__anio}")
        # Acceso directo al método del componente motor (Composición)
        print(f"Especificaciones: {self.__motor.obtener_info_motor()}")
        
    # --- Método acelerar para llamar la función amumentar velocidad ---
    def acelerar(self):
            try:            
                self.velocidad = self.__motor.incrementar_velocidad()
                print(f"la velocidad que incrementa es de: {self.velocidad}")
    
    # --- Captura de errores ---      
            except ValueError as error:
                print(f"error: {error}")
    