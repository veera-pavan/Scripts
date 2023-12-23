#using try/Except block

try:
    division = 10/0
    number = float(input("enter a number: "))
    print(number)
    #here in except blocks we are trying to catch exact error by using expected errro function "ZeroDivisionError/ValueError" and trying to print the actual error
except ZeroDivisionError as err:
    print(err)
except ValueError as err: 
    print(err)
