from models.coche import Coche
from models.motor import Motor # Importamos la nueva clase 

# 1. Primero creamos el motor [cite: 39]
mi_motor_v8 = Motor(450, "V8")

# 2. Creamos el coche y le "ensamblamos" el motor [cite: 5, 86]
mi_auto = Coche("Ford", "Mustang", 2023, mi_motor_v8)

# 3. Mostramos la información completa [cite: 87]
mi_auto.describir()