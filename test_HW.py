import pytest

from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_multiplay_success(self):
        assert self.calc.multiply(self, 1, 0) == 0

    def test_division_success(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 5, 3) == 2
