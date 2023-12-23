
#here we user "and", "or" operands, "elif" is elseif
is_flowerexists = True
isflowere_colourred = True

if is_flowerexists and isflowere_colourred:
    print("plant have flowers and its colour is RED")
#elif is_flowerexists or isflowere_colourred:
    #print("either flower or colour red exists on the plant")
elif is_flowerexists and not(isflowere_colourred):
    print("plant has flours and not colours")
elif not(is_flowerexists) and isflowere_colourred:
    print("coulours exists on plant but no flowers")

else:
    print("plant have no flowers and colours")


#ifstatments with Comparisions and also we have operator like ">=", "<=","==", "!=", ">" & "<"
def highest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(highest(112, 112, 45))

