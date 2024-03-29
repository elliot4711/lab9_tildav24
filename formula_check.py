from linkedQfile import LinkedQ
"""
Na                     Formeln är syntaktiskt korrekt x
H2O                    Formeln är syntaktiskt korrekt x
Si(C3(COOH)2)4(H2O)7   Formeln är syntaktiskt korrekt 
Na332                  Formeln är syntaktiskt korrekt x
C(Xx4)5    Okänd atom vid radslutet 4)5
C(OH4)C    Saknad siffra vid radslutet C
C(OH4C     Saknad högerparentes vid radslutet
H2O)Fe     Felaktig gruppstart vid radslutet )Fe x
H0         För litet tal vid radslutet x
H1C        För litet tal vid radslutet C x
H02C       För litet tal vid radslutet 2C x
Nacl       Saknad stor bokstav vid radslutet cl x
a          Saknad stor bokstav vid radslutet a x
(Cl)2)3    Felaktig gruppstart vid radslutet )3 x
)          Felaktig gruppstart vid radslutet ) x 
2          Felaktig gruppstart vid radslutet 2 x
"""

periodic_table = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 
'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru',
'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu',
'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', "Lv"]

def formula():
    take_input = True
    while take_input == True:
        molecule = input("")
        if molecule == ("#"):
            take_input = False
        else:
            try:
                que = LinkedQ()
                for letter in molecule:
                    que.enqueue(letter)
                returnvalue = ismolecule(que)
                print("Formeln är syntaktiskt korrekt")
            except Syntaxfel as err:
                returnvalue = str(err.args[0])
                print(returnvalue)

def formulatest(molecule):
    try:
        que = LinkedQ()
        for letter in molecule:
            que.enqueue(letter)
        returnvalue = ismolecule(que)
        return("Formeln är syntaktiskt korrekt")
    except Syntaxfel as err:
        returnvalue = str(err.args[0])
        return(returnvalue)


def ismolecule(que):
    que = isgroup(que)
    if not que.isEmpty():
        que = ismolecule(que)

def isgroup(que):
    """ 
    Function for testing if input follows syntax for a molecule
    Parameters: text that could be a molecule
    Returns: nothing
    """
    if que.peek() == None:
        raise Syntaxfel("Enter something")

    if que.peek().isalpha():
        que2 = isatom(que)
        que2 = isnum(que2)
        
        return que2

    elif que.peek() == "(":
        que.dequeue()

        parenthesis_que = LinkedQ()
        while True:
            if que.isEmpty():
                raise Syntaxfel("Saknad högerparentes vid radslutet")
            
            elif que.peek() == "(":
                que = isgroup(que)

            elif que.peek() == ")":
                x = que.dequeue()
                y = que.peek()
                if y == None:
                    break
                elif y.isdigit():
                    break
                else:
                    word = ""
                    if not que.isEmpty():
                        while not que.isEmpty():
                            l = que.dequeue()
                            word += l
                    raise Syntaxfel(f"Saknad siffra vid radslutet {word}")
            else:
                x = que.dequeue()
                parenthesis_que.enqueue(x)
        
        
        isatom(parenthesis_que, que, x)
        que2 = isnum(que)
        return que2

    else:
        word = ""
        if not que.isEmpty():
            while not que.isEmpty():
                l = que.dequeue()
                word += l
            raise Syntaxfel(f"Felaktig gruppstart vid radslutet {word}")
        else:
            raise Syntaxfel("Felaktig gruppstart vid radslutet")


def isatom(que, oldque = None, parenthesis = None):
    """ 
    Function for testing if input follows syntax for an atom
    Parameters: linkedQ object containing all letters and numbers in the atom name
    Returns: linkedQ object with only numbers remaining
    """

    x = que.peek()
    if isbigletter(x):
        x = que.dequeue()
        y = que.peek()
        if que.isEmpty():
            return que
        
        elif not y.isalpha():
            if x in periodic_table:
                isnum(que, oldque, parenthesis)
                return que
            else:
                x = que.dequeue()
                word = x
                while not que.isEmpty():
                    l = que.dequeue()
                    word += l
                if parenthesis != None:
                    word += parenthesis
                if oldque:
                    while not oldque.isEmpty():
                        l = oldque.dequeue()
                        word += l
                raise Syntaxfel(f"Okänd atom vid radslutet {word}")
        
        elif y.isupper():
            if x in periodic_table:
                return que
            else:
                x = que.dequeue()
                word = x
                while not que.isEmpty():
                    l = que.dequeue()
                    word += l
                if parenthesis != None:
                    word += parenthesis
                if oldque:
                    while not oldque.isEmpty():
                        l = oldque.dequeue()
                        word += l
                raise Syntaxfel(f"Okänd atom vid radslutet {word}")
        else:      
            if issmallletter(y):
                que.dequeue()
                word = x + y
                if word in periodic_table:
                    return que
                else:
                    x = que.dequeue()
                    word = x
                    while not que.isEmpty():
                        l = que.dequeue()
                        word += l
                    if parenthesis != None:
                        word += parenthesis
                    if oldque:
                        while not oldque.isEmpty():
                            l = oldque.dequeue()
                            word += l
                    raise Syntaxfel(f"Okänd atom vid radslutet {word}")
            else:
                raise Syntaxfel("Något är fel")
            
    else:
        x = que.dequeue()
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
    if value.isupper():
        return True
    else:
        return False 

def issmallletter(value):
    """ 
    Function for testing if a value is a lowercase letter
    Parameters: value to check
    Returns: True or False
    """
    if value.islower():
        return True
    else:
        return False      

def isnum(que, oldque = None, parenthesis = None):
    """ 
    Function for testing if input follows syntax for a number higher or equal to 2
    Parameters: linkedQ object containing all numbers in the atom name
    Returns: True if number is higher or equal to 2
    """

    if que.peek() == None:
        return que
    
    elif not que.peek().isdigit():
        return que

    else:
        y = que.dequeue()
        if 2 <= int(y) <= 9:
            while not que.isEmpty():
                if que.peek().isdigit():
                    que.dequeue()
                else:
                    break
            return que
        
        elif y == "0":
            word = ""
            if not que.isEmpty():
                if parenthesis != None:
                    while not que.isEmpty():
                        l = que.dequeue()
                        word += l
                    raise Syntaxfel(f"För litet tal vid radslutet {word + parenthesis}")
                else:
                    while not que.isEmpty():
                        l = que.dequeue()
                        word += l
                    raise Syntaxfel(f"För litet tal vid radslutet {word}")
            else:
                if parenthesis != None:
                    if oldque:
                        while not oldque.isEmpty():
                            l = oldque.dequeue()
                            word += l
                        raise Syntaxfel(f"För litet tal vid radslutet {parenthesis + word}")
                    else:
                        raise Syntaxfel(f"För litet tal vid radslutet {parenthesis}")
                else:
                    raise Syntaxfel("För litet tal vid radslutet")
        elif y == "1":
            z = que.peek()
            if z == None:
                if parenthesis != None:
                    if oldque:
                        word = ""
                        while not oldque.isEmpty():
                            l = oldque.dequeue()
                            word += l
                        raise Syntaxfel(f"För litet tal vid radslutet {parenthesis + word}")
                    else:
                        raise Syntaxfel(f"För litet tal vid radslutet {parenthesis}")
                else:
                    raise Syntaxfel("För litet tal vid radslutet")
            else:
                if z.isdigit():
                    while not que.isEmpty():
                        if que.peek().isdigit():
                            que.dequeue()
                        else:
                            break
                    return que
                else:
                    word = ""
                    if not que.isEmpty():
                        while not que.isEmpty():
                            l = que.dequeue()
                            word += l
                        raise Syntaxfel(f"För litet tal vid radslutet {word}")
                    else:
                        if parenthesis != None:
                            raise Syntaxfel(f"För litet tal vid radslutet {parenthesis}")
                        else:
                            raise Syntaxfel("För litet tal vid radslutet")
        else:
            print("fel")

class Syntaxfel(Exception):
    """
    Exception for when syntax is wrong, inherits from Exception
    """

    pass

if __name__ == '__main__':
    formula()