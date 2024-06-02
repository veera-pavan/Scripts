#first define a definetion for Simple Interest formula with relavent variables
#pass values to the above variables using user input
#store the output in to the variable and print the value


def SI_calculator():
    P = int(input("Enter principle amount:"))
    TempInterst_rate = float(input("Enter rate of interest per year:"))
    R = TempInterst_rate / 100
    T = int(input("enter time period in terms of years:"))
    #Simple Interest Formula
    print("input values:" + str(P), str(R), str(T))
    SI = (P*R*T)
    print(SI)
    print("Simple Interest:" + str(int(SI)))

SI_calculator()

