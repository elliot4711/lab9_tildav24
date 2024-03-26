from linkedQfile import LinkedQ

periodic_table = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 
'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru',
'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu',
'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', "Lv"]

pattern = r'\(|\)'

def ismolecule(molecule):
    """ 
    Function for testing if input follows syntax for a molecule
    Parameters: text that could be a molecule
    Returns: nothing
    """

    que = LinkedQ()
    for letter in molecule:
        que.enqueue(letter)

    que2 = isatom(que)
    isnum(que2)
    print("Formeln är syntaktiskt korrekt")

def isatom(que):
    """ 
    Function for testing if input follows syntax for an atom
    Parameters: linkedQ object containing all letters and numbers in the atom name
    Returns: linkedQ object with only numbers remaining
    """

    x = que.peek()
    if isbigletter(x):
        x = que.dequeue()
        y = que.peek()
        if y == None:
            return que
        else: 
            if y.isdigit():
                return que
            
            else:
                if issmallletter(y):
                    que.dequeue()
                    return que
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

def isnum(que):
    """ 
    Function for testing if input follows syntax for a number higher or equal to 2
    Parameters: linkedQ object containing all numbers in the atom name
    Returns: True if number is higher or equal to 2
    """

    if que.peek() == None:
        return 

    else:
        y = que.dequeue()
        if 2 <= int(y) <= 9:
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
            z = que.peek()
            if z == None:
                raise Syntaxfel("För litet tal vid radslutet")
            else:
                if z.isdigit():
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


take_input = True
while take_input == True:
    molecule = input("")
    if molecule == ("#"):
        take_input = False
    else:
        try:
            returnvalue = ismolecule(molecule)
        except Syntaxfel as err:
            returnvalue = str(err.args[0])
            print(returnvalue)
