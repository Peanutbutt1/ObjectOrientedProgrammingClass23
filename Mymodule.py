#Now we are going to make our own commands like in math liberary

class Math1:
    
    @staticmethod     
    def add1(x, y):
        return x + y
    
    @staticmethod
    def sub1(x, y):
        return x - y
    
    @staticmethod
    def mult1(x, y):
        return x * y
    
    @staticmethod
    def devide1(x, y):
        return round(x / y, 2)
    
    @staticmethod
    def average1(x, y):
        return round((x + y) / 2, 2)
    
    @staticmethod
    def percentage1(x, y):
        return round((x / y) * 100, 2)
    
    @staticmethod
    def add19(x, y):
        return (x, y) + 19