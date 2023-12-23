
#print(2**3)-----> this means 2 to the power or 3 that is 2*2*2 = 8
#defining a function to mimic exponential functionality using user input

base_num = input('enter base number:')
pow_num = input('enter power number:')
def exponential(base_num, pow_num):
    result = 1
    for expo in range(int(pow_num)):
        result = result*int(base_num)
    return result

print(exponential(base_num, pow_num))




