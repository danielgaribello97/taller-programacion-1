#Esta es la forma de como se importan las clases al archivo principal
from models.coche import Coche
from models.motor import Motor # Importamos la nueva clase 
from models.animal.Ave import Ave
from models.animal.Gato import Gato
from models.animal.Perro import Perro


# 1. Primero creamos el motor [cite: 39]
mi_motor_v8 = Motor(450, "V8", 300)


# 2. Creamos el coche y le "ensamblamos" el motor [cite: 5, 86]
mi_auto = Coche("Ford", "Mustang", 2023, mi_motor_v8)

# 3. Mostramos la información completa [cite: 87]
mi_auto.describir()

# 10. Mostramos el aumento de velocidad
mi_auto.acelerar()


# 7 Creamos las instancias de los diferentes animales haciendo uso de la clase abstracta Animal donde llamamos su metodo abstracto hacersonido

# Hacemos uso del metodo abstracto hacersonido de cada animal
perro = Perro()
perro.set_hacersonido()

gato = Gato()
gato.set_hacersonido()

ave = Ave()
ave.set_hacersonido()

