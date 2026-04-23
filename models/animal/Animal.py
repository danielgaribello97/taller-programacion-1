
from abc import ABC, abstractmethod

class Animal(ABC): 
    """
    Clase crea clase base para la gestión de animales tipo Animal.
    Implementa validación con un método abstracto hacerSonido para los diferentes animales 
    Esta clase se define como abstracta porque contien dos modulos que son ABC y abstractmethod que nos indica que es una clase abstracta con metodos 
    """

@abstractmethod
# método que cada animal debe implementar
def set_hacersonido(self):
    pass
