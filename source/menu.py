#Author: Nathanael Gordon
#Created: 2014-12-16

class Menu:
    
    def __init__(self, exitString = "Return to previous menu", title = "Tournamenter"):
        self.options = []
        self.title = title
        self.exitString = exitString
    
    def printMenu(self, values):
        validResult = False
        
        while not validResult:
            count = 1
            result = -1
            
            print(self.title)
            
            for tup, func in self.options:
                print("{0} - {1}".format(count, tup))
                count += 1
                
            print("0 - {0}\n".format(self.exitString))
            
            try:
                result = int(input("Selection: "))
                if result < 0 or result >= count: #must be >= since count with be one greater than the largest number printed
                    raise ValueError()
                
                validResult = True
            except ValueError:
                print("\nPlease enter a number in the range of 0 - {0}\n".format(count-1))
        
        if result > 0:
            return self.options[result - 1][1](values, result)
        else:
            return -1
    
    def addOption(self, string, func):
        self.options.append((string, func))
    
def confirm(questionToConfirm, yes = "Yes", no = "No"):
    validResult = False
        
    while not validResult:
        
        print(questionToConfirm)
        print("1 - {0}".format(yes))
        print("0 - {0}".format(no))
        
        try:
            result = int(input("Selection: "))
            if result < 0 or result > 1: #must be >= since count with be one greater than the largest number printed
                raise ValueError()
            
            validResult = True
        except ValueError:
            print("\nPlease enter a number in the range of 0 - {0}\n".format(count-1))
    
    return result == 1