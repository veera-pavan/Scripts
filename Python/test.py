#Guessing Game
guess_name = ''
secret_name = "Galaxy"
loop_limit = 3
loop_count = 0
while guess_name != secret_name and loop_count < loop_limit:
    guess_name = input("Guess secret name:")
    #print("you lose")  
    loop_count += 1
    print("your " + str(loop_count)+ " attempt completed")
      
if guess_name == secret_name:
    print("That's right,You Won the Game")
else:
    print("You Lose")

#other way arround

guess_name = ''
secret_name = "Galaxy"
loop_limit = 3
loop_count = 0
out_of_guesses = False
while guess_name != secret_name and not(out_of_guesses):
    if loop_count < loop_limit:
        guess_name = input("Guess secret name:") 
        loop_count += 1
        print("your " + str(loop_count)+ " attempt completed")
    else:
        out_of_guesses = True
        
      
if out_of_guesses:
    print("You Lose")
else:
    print("You Win")



