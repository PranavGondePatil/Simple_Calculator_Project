# Calculator Project (By my own Creative Thoughts and Logic)

class Calculator :
    
    # Taking Two number as an Inputs for performing furthur Operations
    num1 = int(input('Enter a Number 1 : '))
    num2 = int(input('Enter a Number 2 : '))
    
    # Function for Addition
    def Addition(self) :
        a = self.num1 + self.num2
        print(f"The result of the Addition is {a}")
        
    # Function for Substraction
    def Substraction(self) :
        a = self.num1 - self.num2
        print(f"The result of the Substraction is {a}")
        
    # Function for Multiplication  
    def Multiplication(self) :
        a = self.num1 * self.num2
        print(f"The result of the Multiplication is {a}")
    
    # Function for Division
    def Division(self) :
        if(self.num1 and self.num2 != 0) :
            a = self.num1 / self.num2
            print(f"The result of the Division is {a}")
        else : 
            print("Enter numbers other than Zero(0)")
        
    # Function for Modulus
    def Modulus(self) :
        a = self.num1 % self.num2
        print(f"The result of the Modules is {a}")
    
    
calculatorObj = Calculator()

displayOperation = '''
              =====Weclcome to Simple Calculator=====
    ***Choose the Following Option to Perform the Operations***
         
         1. Addition
         2. Substraction
         3. Multiplication
         4. Division
         5. Modules
         6. Exit

'''

print(displayOperation)

while(True) :
    choice = int(input("Enter Your Choice : "))

    if(choice == 1) :
        # This will Invoke Addition Function of class Calculator
        calculatorObj.Addition() 
    
    elif(choice == 2) :
        # This will Invoke Substraction Function of class Calculator
        calculatorObj.Substraction()
        
    elif(choice == 3) :
        # This will Invoke Multiplication Function of class Calculator
        calculatorObj.Multiplication()
        
    elif(choice == 4) :
        # This will Invoke Division Function of class Calculator
        calculatorObj.Division()
        
    elif(choice == 5) :
        # This will Invoke Modulus Function of class Calculator
        calculatorObj.Modulus()
        
    elif(choice == 6) :
        # This will Exit the Program
        print("The Program has been Exited")
        exit()
        
    else :
        print("Invalid Choice")
