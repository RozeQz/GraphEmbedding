from abc import ABC, abstractmethod

class Algorithm(ABC):
    """Абстрактный класс для алгоритмов."""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass
