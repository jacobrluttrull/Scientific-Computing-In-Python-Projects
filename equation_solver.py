from abc import ABC, abstractmethod


class Equation(ABC):
    degree: int

    def __init__(self, *args):
        pass

    def __init_subclass__(cls):
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )

    @abstractmethod
    def solve(self):
        pass

    @abstractmethod
    def analyze(self):
        pass


class LinearEquation(Equation):
    degree = 1

    def solve(self):
        pass

    def analyze(self):
        pass


lin_eq = LinearEquation()