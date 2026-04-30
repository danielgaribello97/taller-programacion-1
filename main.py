from models.coche import Coche
from models.motor import Motor 
from models.Bicicleta import Bicicleta # Nueva importación[cite: 11]
from models.animal.Ave import Ave
from models.animal.Gato import Gato
from models.animal.Perro import Perro
from models.animal.Interfaces.Pajaro import Pajaro
from models.animal.Interfaces.Avion import Avion

# --- Pruebas de Coche y Motor (Puntos 1, 2, 3, 9 y 10) ---
mi_motor_v8 = Motor(450, "V8", 100) # Bajamos a 100 para probar aceleración normal
mi_auto = Coche("Ford", "Mustang", 2023, mi_motor_v8)

mi_auto.describir()
mi_auto.acelerar()

# --- Pruebas de Animales (Punto 7) ---
perro = Perro()
perro.set_hacersonido()

gato = Gato()
gato.set_hacersonido()

ave = Ave()
ave.set_hacersonido()


# Lista que contiene diferentes tipos de vehículos[cite: 11]
mis_transportes = [
    mi_auto,
    Bicicleta("GW", "Raven", "Ruta"),
    Bicicleta("Shimano", "Deore", "Montaña")
]

# Ejecución polimórfica del método acelerar[cite: 11]
for v in mis_transportes:
    v.acelerar()


pajaro_test = Pajaro()
avion_test = Avion()

pajaro_test.volar()
avion_test.volar()
