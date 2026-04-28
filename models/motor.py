class Motor:
    # Agregamos 'velocidad' aquí para que acepte los 3 datos del main
    def __init__(self, potencia, tipo, velocidad):
        self.__potencia = potencia
        self.__tipo = tipo
        self.__velocidad = velocidad

    def obtener_info_motor(self):
        return f"Motor {self.__tipo} con {self.__potencia} HP"
    
    def incrementar_velocidad(self):
        if self.__velocidad < 0:
            raise ValueError("la velocidad no puede ser negativa")
        if self.__velocidad >= 200:
            return f"Velocidad maxima excedida: {self.__velocidad}"
        return self.__velocidad + 5