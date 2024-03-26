import unittest

from parameterized import parameterized
from linkedQfile import LinkedQ
import re

def ismolecule(molecule):
    """ 
    Function for testing if input follows syntax for a molecule
    Parameters: text that could be a molecule
    Returns: string object
    """

    x = re.search(r'\d', molecule)
    que = LinkedQ()
    for letter in molecule:
        que.enqueue(letter)

    if x:
        que2 = isatom(que)
        isnum(que2)
        return("Formeln är syntaktiskt korrekt")
    
    else:
        isatom(que)
        return("Formeln är syntaktiskt korrekt")
    

def isatom(que):
    """ 
    Function for testing if input follows syntax for an atom
    Parameters: linkedQ object containing all letters and numbers in the atom name
    Returns: linkedQ object with only numbers remaining
    """

    y = que.peek()
    x = que.dequeue()
    if isbigletter(x):
        if y == None:
            return que
        else: 
            z = re.search(r'\d', y)
            if z:
                return que
            
            else:
                y = que.dequeue()
                if issmallletter(y):
                    return que
                else:
                    raise Syntaxfel("Något är fel")
            
    else:
        word = x
        while not que.isEmpty():
            l = que.dequeue()
            word += l
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {word}")


def isbigletter(value):
    """ 
    Function for testing if a value is a capital letter
    Parameters: value to check
    Returns: True or False
    """

    x = re.search("[A-Z]", value)
    if x:
        return True
    else:
        return False 

def issmallletter(value):
    """ 
    Function for testing if a value is a lowercase letter
    Parameters: value to check
    Returns: True or False
    """

    x = re.search("[a-z]", value)
    if x:
        return True
    else:
        return False      

def isnum(que):
    """ 
    Function for testing if input follows syntax for a number higher or equal to 2
    Parameters: linkedQ object containing all numbers in the atom name
    Returns: True if number is higher or equal to 2
    """

    z = que.peek()
    y = que.dequeue()
    x = re.search("[2-9]", y)
    if x:
        return True
    elif y == "0":
        word = ""
        if not que.isEmpty():
            while not que.isEmpty():
                l = que.dequeue()
                word += l
            raise Syntaxfel(f"För litet tal vid radslutet {word}")
        else:
            raise Syntaxfel("För litet tal vid radslutet")
    elif y == "1":
        if z == None:
            raise Syntaxfel("För litet tal vid radslutet")
        else:
            number = re.search(r'\d', z) #Skapar problem
            if number:
                pass
            else:
                raise Syntaxfel("För litet tal vid radslutet")
    else:
        print("fel")

class Syntaxfel(Exception):
    """
    Exception for when syntax is wrong, inherits from Exception
    """

    pass


def testfunc(molecule):
    """
    Function for testing syntax functions. Runs function and captures answer
    Parameters: string to check if it is a molecule
    Returns: Answer from functions
    """

    try:
        value = ismolecule(molecule)
        return value
    except Syntaxfel as err:
        returnvalue = str(err.args[0])
        return returnvalue


class TestSequence(unittest.TestCase):
    @parameterized.expand([
        ["1", testfunc("Na"), "Formeln är syntaktiskt korrekt",],
        ["2", testfunc("H2O"), "Formeln är syntaktiskt korrekt"],
        ["3", testfunc("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt"],
        ["4", testfunc("Na332"), "Formeln är syntaktiskt korrekt",],
        ["5", testfunc("C(Xx4)5"), "Okänd atom vid radslutet 4)5"],
        ["6", testfunc("C(OH4)C"), "Saknad siffra vid radslutet C"],
        ["7", testfunc("C(OH4C"), "Saknad högerparentes vid radslutet",],
        ["8", testfunc("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe"],
        ["9", testfunc("H0"), "För litet tal vid radslutet"],
        ["10", testfunc("H1C"), "För litet tal vid radslutet C",],
        ["11", testfunc("H02C"), "För litet tal vid radslutet 2C"],
        ["12", testfunc("Nacl"), "Saknad stor bokstav vid radslutet cl"],
        ["13", testfunc("a"), "Saknad stor bokstav vid radslutet a",],
        ["14", testfunc("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3"],
        ["15", testfunc(")"), "Felaktig gruppstart vid radslutet )"],
        ["16", testfunc("2"), "Felaktig gruppstart vid radslutet 2",],
    ])
    def test_sequence(self, name, a, b):
        self.assertEqual(a,b)

if __name__ == '__main__':
    unittest.main()


