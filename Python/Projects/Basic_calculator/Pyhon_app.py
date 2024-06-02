#here firt we define function for add, sub, mul and div
#ask user input 
# perform calculations

def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")
def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer) + "\n")
def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer) + "\n")
def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer) + "\n")

while True:
    print("A.addition")
    print("B.substraction")
    print("C.multiplication")
    print("D.division")
    print("E.exit")

    calculator = input("enter the math operation you want to perform:")

    if calculator == "A" or calculator == "a":
        a = int(input("enter first value:"))
        b = int(input("enter second value:"))
        add(a, b)
    elif calculator == "B" or calculator == "b":
        a = int(input("enter first value:"))
        b = int(input("enter second value:"))
        sub(a, b)
    elif calculator == "C" or calculator == "c":
        a = int(input("enter first value:"))
        b = int(input("enter second value:"))
        mul(a, b)
    elif calculator == "D" or calculator == "d":
        a = int(input("enter first value:"))
        b = int(input("enter second value:"))
        div(a, b)
    elif calculator == "E" or calculator == "e":
        quit()


    

