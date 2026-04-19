class Motor:
    # Definimos los atributos básicos del motor [cite: 85]
    def __init__(self, potencia, tipo):
        self.__potencia = potencia
        self.__tipo = tipo

    # Método para devolver los datos del motor [cite: 87]
    def obtener_info_motor(self):
        return f"Motor {self.__tipo} con {self.__potencia} HP"