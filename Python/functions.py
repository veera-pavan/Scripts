def sample():
    print("hello world")

sample()

#now let try passing parameters to the sample function

def sample1(name):
    print("hello world " + name)

sample1("Panjagala Pavan")

#now lets try by passing integer

def sample2(name, age):
    print("hello world " + name + " your are at " + str(age))

sample2("Panjagala Pavan", 29)

#functions using userinput example
def powerofthree():
    user_input = input("enter the power of 3:")
    print(user_input)
    result = pow(3, int(user_input))
    print("result:" + str(result))
powerofthree()