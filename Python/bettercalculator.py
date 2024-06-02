num1 = float(input("enter first number: "))
op = input("enter operator: ")
print (op)
num2 = float(input("enter second number: "))

def calculator():
        if op == "*":
            return num1*num2
        elif op == "/":
            return num1/num2
        elif op == "+":
            return num1+num2
        elif op == "-":
            return num1-num2
        elif op == "%":
             return num1%num2
        else:
             return "invalid operator"
print(calculator())