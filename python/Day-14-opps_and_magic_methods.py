# magic methods are the methods that are defined inside the class and are used to perform special operations


class Frection:
    def __init__(self, numerator, demoninator):
        # instance variables are the variables that are defined inside the instance of the class
        #  we can make private using __ before the variable name
        self.num = numerator
        # or self.__num =numerator
        self.den = demoninator
        # or self.__den = demoninator --- to make it private

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self):
        return f"{self.num + self.den}"
    
    def __sub__(self):
        return f"{self.num - self.den}"
    
    def __mul__(self):
        return f"{self.num * self.den}"
    
    def __truediv__(self):
        return f"{self.num / self.den}"
    
    def __floordiv__(self):
        return f"{self.num // self.den}"
    
    def __mod__(self):
        return f"{self.num % self.den}"
    
    def __pow__(self):
        return f"{self.num ** self.den}"
    
    def __lt__(self, other):
        return f"{self.num < other.num}"    # less than
    
    def __gt__(self, other):
        return f"{self.num > other.num}"    # greater than 
    
    def __eq__(self, other):
        return f"{self.num == other.num}"
    
    def __ne__(self, other):
        return f"{self.num != other.num}"    # not equal to
    

    def __le__(self, other):
        return f"{self.num <= other.num}"    # less than or equal to
    
    def __ge__(self, other):
        return f"{self.num >= other.num}"    # greater than or equal to
    
    def __neg__(self):
        return f"{-self.num}"    # negative
    
    def __pos__(self):
        return f"{+self.num}"    # positive

    def __abs__(self):
        return f"{abs(self.num)}"    # absolute value