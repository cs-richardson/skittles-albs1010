#Albert
'''
The code generates a random number between -1 and 1024. It then asks the user
to guess the number. If the user guesses wrong, the program will keep on asking
the user with certain hints until the user guesses right.
'''
import random
random_number = random.randint(0,1023)

guess = int(input("O hai! I'm thinking of a number between 0 and 1023. What is it?\n"))

while guess != random_number:
    
#Hints that helps the user guess more accurately
    
    if guess > random_number and guess < 1023:
        print("Nope! There are fewer Skittles than that. Guess again.")
        
    elif guess < random_number and guess > -1:
        print("Nope! There are way more Skittles than that. Guess again.")

    else:
        print("Nope! Don't be difficult. Guess again.")
    
    guess = int(input(""))
    

print("That's right! Nom nom nom")
