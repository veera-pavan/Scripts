#Ask user if they want to generate a pwd or not
#If yes ask for length of the pwd
#Generate password
#Print Password
#If initial respone is "No", exit the program.

Pwdgeneratorinput = input("You want to generate password(Yes/No): ")
Pwdgenerator = Pwdgeneratorinput.lower()

print(Pwdgenerator)
if Pwdgenerator == "yes":
    # import the string and random modules
    import string
    import random

    # define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # or you can use below changed version of puncuations you can use of your own

    #all_characters = string.ascii_letters + string.digits + "@*()"

    # ask the user for the desired length of the password
    length = int(input("Enter the length of the password: "))

    # generate a password using randomly chosen characters
    # using the 'choices' function from the random module
    # and joining the resulting characters into a string
    password = ''.join(random.choices(all_characters, k=length))

    # display the generated password to the user
    print("Your password is:", password)
else:
    exit()