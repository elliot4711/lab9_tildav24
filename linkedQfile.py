class Node:
    """
    Class for node object
    """

    def __init__(self, value, next=None):
        """
        Constructor for node object with value and reference to next
        Parameters: self, value, next(None if not specified)
        Returns: nothing
        """
        
        self.value = value
        self.next = next

    def get_elements(self):
        """
        Gives value of element
        Parameters: self
        Returns: value of element
        """

        return self.value

class LinkedQ:
    """
    Class for a linked queue
    """

    def __init__(self):
        """
        Constructor for linked queue
        Parameters: self
        Returns: nothing
        """

        self.__first = None
        self.__last = None

    def __str__(self):
        """
        Returns string of every queue element for printing
        Parameters: self
        Returns: String of all queue elements
        """

        x = ""
        z = ""
        y = self.__first
        count = 1
        while y != None :
            x = (y.get_elements())
            z = z + x
            y = y.next
            count+=1
        return z


    def enqueue(self, value):
        """
        Function that adds value to the end of the queue
        Parameters: self, value(to be added)
        Returns: nothing
        """

        new = Node(value)
        if self.__first == None:
            self.__first = new
            self.__last = new

        else:
            self.__last.next = new
            self.__last = new
    
    def isEmpty(self):
        """
        Function that checks if array is empty
        Parameters: self
        Returns: True if list is empty, False if not
        """

        if self.__first == None:
            return True
        else:
            return False
        
    def dequeue(self):
        """
        Function that removes the first value in the queue and returns its value
        Parameters: self
        Returns: Removed object
        """

        if not self.isEmpty():
            x = self.__first.get_elements()
            self.__first = self.__first.next

            return x
        else:
            return "Queue is empty"
        
    def size(self):
        """
        Function that checks the lenght of the queue
        Parameters: self
        Returns: Lenght of queue
        """

        y = self.__first
        lenght = 0 
        while y:
            lenght += 1
            y = y.next
        return lenght
    
    def show(self):
        """
        Function that displays the values of all elements and their positions (from stackoverflow)
        Parameters: self
        Returns: nothing
        """

        y = self.__first
        count = 1
        while y != None :
            print('Entry # ', count, '=', y.get_elements()) 
            y = y.next
            count+=1
    
    def peek(self):
        """
        Function that looks at the next value without dequeuing it
        Parameters: nothing
        Returns: value on next pointer
        """

        try:
            x = self.__first.get_elements()
            return x
        except:
            return None

            
