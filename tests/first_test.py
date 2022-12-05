import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_correct(self):
        assert self.calc.division(self, 20, 5) == 4

    def test_subtraction_correct(self):
        assert self.calc.subtraction(self, 300, 150) == 150

    def test_adding_correct(self):
        assert self.calc.adding(self, 10, 10) == 20