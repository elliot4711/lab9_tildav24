import unittest

from parameterized import parameterized
from linkedQfile import LinkedQ
import re

from formula_check import formulatest

class TestSequence(unittest.TestCase):
    @parameterized.expand([
        ["1", formulatest("Na"), "Formeln är syntaktiskt korrekt"],
        ["2", formulatest("H2O"), "Formeln är syntaktiskt korrekt"],
        ["3", formulatest("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt"],
        ["4", formulatest("Na332"), "Formeln är syntaktiskt korrekt"],
        ["5", formulatest("C(Xx4)5"), "Okänd atom vid radslutet 4)5"],
        ["6", formulatest("C(OH4)C"), "Saknad siffra vid radslutet C"],
        ["7", formulatest("C(OH4C"), "Saknad högerparentes vid radslutet"],
        ["8", formulatest("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe"],
        ["9", formulatest("H0"), "För litet tal vid radslutet"],
        ["10", formulatest("H1C"), "För litet tal vid radslutet C"],
        ["11", formulatest("H02C"), "För litet tal vid radslutet 2C"],
        ["12", formulatest("Nacl"), "Saknad stor bokstav vid radslutet cl"],
        ["13", formulatest("a"), "Saknad stor bokstav vid radslutet a"],
        ["14", formulatest("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3"],
        ["15", formulatest(")"), "Felaktig gruppstart vid radslutet )"],
        ["16", formulatest("2"), "Felaktig gruppstart vid radslutet 2"],
    ])
    def test_sequence(self, name, a, b):
        self.assertEqual(a,b)

if __name__ == '__main__':
    unittest.main()


