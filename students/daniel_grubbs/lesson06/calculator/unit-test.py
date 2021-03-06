from unittest import TestCase
from unittest.mock import MagicMock

from adder import Adder
from subtracter import Subtracter
from multiplier import Multiplier
from divider import Divider
from calculator import Calculator
from exceptions import InsufficientOperands


class AdderTest(TestCase):

    def test_adding(self):
        adder = Adder()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i + j, adder.calc(i, j))


class SubtracterTest(TestCase):

    def test_subtracting(self):
        subtracter = Subtracter()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i - j, subtracter.calc(i, j))


# Do the test for multiplier and divider
class MultiplierTest(TestCase):

    def test_multiplying(self):
        multiplier = Multiplier()

        for i in range(-10, 10):
            for j in range(-10, 10):
                self.assertEqual(i * j, multiplier.calc(i, j))


class DividerTest(TestCase):

    def test_dividing(self):
        divider = Divider()

        for i in range(-10, 10):
            for j in range(-10, 10):
                # print(i, j)
                if i == 0 or j == 0:
                    continue

                self.assertEqual(i // j, divider.calc(i, j))


#
class CalculatorTests(TestCase):

    def setUp(self):
        self.adder = Adder()
        self.subtracter = Subtracter()
        self.multiplier = Multiplier()
        self.divider = Divider()

        self.calculator = Calculator(self.adder, self.subtracter, self.multiplier, self.divider)

    def test_adder_call(self):
        self.adder.calc = MagicMock(return_value=0)

        # self.calculator.enter_number(2)
        # self.calculator.enter_number(1)
        # The order needed to be changed because they are applied bottom up
        self.calculator.enter_number(2)
        self.calculator.enter_number(1)
        self.calculator.add()

        self.adder.calc.assert_called_with(1, 2)

    def test_subtracter_call(self):
        self.subtracter.calc = MagicMock(return_value=0)

        self.calculator.enter_number(2)
        self.calculator.enter_number(1)
        self.calculator.subtract()

        self.subtracter.calc.assert_called_with(1, 2)

    def test_multiplier_call(self):
        self.multiplier.calc = MagicMock(return_value=0)

        self.calculator.enter_number(2)
        self.calculator.enter_number(1)
        self.calculator.multiply()

        self.multiplier.calc.assert_called_with(1, 2)

    def test_divider_call(self):
        self.divider.calc = MagicMock(return_value=0)

        self.calculator.enter_number(2)
        self.calculator.enter_number(1)
        self.calculator.divide()

        self.divider.calc.assert_called_with(1, 2)

    def test_insufficient_operands(self):
        self.calculator.enter_number(0)

        with self.assertRaises(InsufficientOperands):
            self.calculator.add()
