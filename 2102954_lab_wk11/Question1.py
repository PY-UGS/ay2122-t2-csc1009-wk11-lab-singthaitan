class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def adder(self):
        print("Addition:")
        print(self.num1+self.num2)

    def subtractor(self):
        print("Subtraction:")
        print(self.num1-self.num2)

    def multiplier(self):
        print("Multiplication:")
        print(self.num1*self.num2)

    def divider(self):
        print("Division:")
        print(self.num1/self.num2)

    def clear(self):
        self.num1 = 0
        self.num2 = 0
        print("Clear: num1: "+ str(self.num1) + "   num2: "+ str(self.num2))
        



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
calculator = Calculator(num1, num2)
calculator.adder()
calculator.subtractor()
calculator.multiplier()
calculator.divider()
calculator.clear()

