class Motor:
    # Definimos los atributos básicos del motor [cite: 85]
    def __init__(self, potencia, tipo, velocidad):
        self.__potencia = potencia
        self.__tipo = tipo
        self.__velocidad = velocidad

    # Método para devolver los datos del motor [cite: 87]
    def obtener_info_motor(self):
        return f"Motor {self.__tipo} con {self.__potencia} HP"
    
    # metodo aumentar velocidad del coche
    def incrementar_velocidad(self):
        if self.__velocidad < 0:
            raise ValueError ("la velocidad no puede ser negativa")
        if self.__velocidad >= 200:
            return f"Velocidad maxima excedida: {self.__velocidad}"
        return self.__velocidad + 5

        
    
        