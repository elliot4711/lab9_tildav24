from linkedQfile import LinkedQ

periodic_table = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 
'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni',
'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru',
'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu',
'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', "Lv"]

DEBUG = True

class Syntaxfel(Exception):
    """
    Exception for when syntax is wrong, inherits from Exception
    """

    pass

def formula():
    if DEBUG:
        print("formula")
    
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
    if DEBUG:
        print("ismolecule")
    que = isgroup(que)
    if not que.isEmpty():
        que = ismolecule(que)
    return que

def isgroup(que):
    """ 
    Function for testing if input follows syntax for a molecule
    Parameters: text that could be a molecule
    Returns: nothing
    """
    if DEBUG:
        print("isgroup")
        print(que)
    
    if que.peek() is None:
        raise Syntaxfel("Enter something")

    elif que.peek().isalpha():
        que = isatom(que)
        que = isnum(que)
        return que
    
    elif que.peek() == "(":
        que = parenthesishandling(que)
        return que
   
    else:
        word = get_word(que)
        raise Syntaxfel(f"Felaktig gruppstart vid radslutet {word}")

    
def parenthesishandling(que):
    if DEBUG:
        print("parenthesishandling")
        print(que)

    que.dequeue()

    if que.peek() == "(":
        que = parenthesishandling(que)

    elif que.peek().isalpha():
        while not que.isEmpty():
            que = isatom(que)
            que = isnum(que)

            if que.peek() == "(":
                que = parenthesishandling(que)

            if que.peek() == (")"):
                que.dequeue()
                if que.isEmpty():
                    word = get_word(que)
                    raise Syntaxfel(f"Saknad siffra vid radslutet {word}")
                    
                elif que.peek().isdigit():
                    que = isnum(que)
                    return que
                
                else:
                    word = get_word(que)
                    raise Syntaxfel(f"Saknad siffra vid radslutet {word}")

        word = get_word(que)
        raise Syntaxfel(f"Saknad högerparentes vid radslutet {word}") 
    
    else:
        word = get_word(que)
        raise Syntaxfel(f"Felaktig gruppstart vid radslutet {word}")
           
      

def isatom(que):
    if DEBUG:
        print("isatom")

    firstletter = que.peek()
    if isbigletter(firstletter):
        que.dequeue()
        secondletter = que.peek()
        if secondletter == None or not secondletter.isalpha():
            if firstletter in periodic_table:
                return que
            else: 
                word = get_word(que)
                raise Syntaxfel(f"Okänd atom vid radslutet {word}")


        elif issmallletter(secondletter):
            secondletter = que.dequeue()
            atom = firstletter + secondletter
            if atom in periodic_table:
                return que
            else:
                word = get_word(que)
                raise Syntaxfel(f"Okänd atom vid radslutet {word}")
        
        else:
            if firstletter in periodic_table:
                return que
            else:
                word = get_word(que)
                raise Syntaxfel(f"Okänd atom vid radslutet {word}")
    
    else:
        word = get_word(que)
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {word}")
    
def isnum(que):
    if DEBUG:
        print("isnum")

    if que.isEmpty() or que.peek() is None:
        return que
    
    elif not que.peek().isdigit():
        return que
    
    else:
        if que.peek() == "0":
            que.dequeue()
            word = get_word(que)
            raise Syntaxfel(f"För litet tal vid radslutet {word}")

        else:
            number = ""
            while not que.isEmpty() and que.peek().isdigit():
                number += que.dequeue()
            number = int(number)

            if number >= 2:
                return que
            
            else:
                word = get_word(que)
                raise Syntaxfel(f"För litet tal vid radslutet {word}")

def isbigletter(value):
    """ 
    Function for testing if a value is a capital letter
    Parameters: value to check
    Returns: True or False
    """
    if DEBUG:
        print("isbigletter")

    if value is not None:
        return value.isupper()
    else:
        return False 

def issmallletter(value):
    """ 
    Function for testing if a value is a lowercase letter
    Parameters: value to check
    Returns: True or False
    """
    
    if DEBUG:
        print("issmallletter")

    if value is not None:
        return value.islower()
    else:
        return False 

def get_word(que):
    word = ""
    if not que.isEmpty():
        while not que.isEmpty():
            l = que.dequeue()
            word += l
    return word

if __name__ == '__main__':
    formula()