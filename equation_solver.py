from abc import ABC
from abc import abstractmethod


class Equation(ABC):
    @abstractmethod
    def solve(self):
        pass

    @abstractmethod
    def analyze(self):
        pass


class LinearEquation(Equation):
    pass


lin_eq = LinearEquation()