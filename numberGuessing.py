import random

#Game to guess a random number
print("""Welcome to the guessing game
the number will be between 0-10""")

rand_answer = random.randint(0,10)
player_guess = input("What is your guess? ")


while rand_answer != int(player_guess):
    player_guess = input("What is your guess? ")
    if(int(player_guess) != rand_answer):
        print('Wrong answer, the correct answer is ' + str(rand_answer))
    elif(int(player_guess) == rand_answer):
        print('Correct guess')
        
print('random number is ' + str(rand_answer))
print('number guessed ' + str(player_guess))