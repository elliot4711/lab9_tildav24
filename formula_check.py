from linkedQfile import LinkedQ
import re

periodic_table = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 
'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru',
'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu',
'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', "Lv"]

pattern = r'\(|\)'

def store_formula(text):
    que = LinkedQ
    for letter in text:
        que.enqueue(letter)
    return que

def ismol(que1, text):
    que1 = isgroup(que1, text)
    if que1.isempty():
        print("Formeln är syntaktiskt korrekt")
    else:
        que1, text = ismol(que1, text)


def isgroup(que1, text):
    """ 
    Function for testing if input follows syntax for a molecule
    Parameters: text that could be a molecule
    Returns: nothing
    """
    que = LinkedQ()
    quenew = LinkedQ

    parenthesis = re.search(pattern, text)
    if parenthesis: 
        letter = que.dequeue()
        while letter != ")":
            letter = que.dequeue()
            quenew.enqueue(letter)
        quenew = ismol(quenew)
        que = isnum(que)
        return quenew

    else:
        x = re.search(r'\d', text)

        if x:
            que2 = isatom(que)
            que2 = isnum(que2)
            return que2
        
        else:
            isatom(que)
    

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
            if x in periodic_table:
                return que
            else:
                word = x
                while not que.isEmpty():
                    l = que.dequeue()
                    word += l
                raise Syntaxfel(f"Okänd atom vid radslutet {word}")
        else: 
            z = re.search(r'\d', y)
            if z:
                if x in periodic_table:
                    return que
                else:
                    word = x
                    while not que.isEmpty():
                        l = que.dequeue()
                        word += l
                    raise Syntaxfel(f"Okänd atom vid radslutet {word}")
            
            else:
                y = que.dequeue()
                if issmallletter(y):
                    atomname = x + y
                    if atomname in periodic_table:
                        return que
                    else:
                        word = ""
                        while not que.isEmpty():
                            l = que.dequeue()
                            word += l
                        raise Syntaxfel(f"Okänd atom vid radslutet {word}")
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
            number = re.search(r'\d', z)
            if number:
                return que
            else:
                raise Syntaxfel("För litet tal vid radslutet")
    else:
        print("fel")

class Syntaxfel(Exception):
    """
    Exception for when syntax is wrong, inherits from Exception
    """

    pass

def formel():
    take_input = True
    while take_input == True:
        text = input("")
        if text == ("#"):
            take_input = False
        else:
            try:
                que1 = store_formula(text)
                returnvalue = ismol(que1, text)
            except Syntaxfel as err:
                returnvalue = str(err.args[0])
                print(returnvalue)

formel()