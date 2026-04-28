from abc import ABC, abstractmethod

class Volador(ABC):
    @abstractmethod
    def volar(self):
        """Interfaz para definir la acción de volar"""
        pass