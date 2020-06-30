class Calculator:
    num = 100

    def __init__(self):
        print("constructor")

    def getta(self):
        print("I am class")


obj = Calculator()
obj.getta()
print(obj.num)