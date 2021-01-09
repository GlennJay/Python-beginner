import random

#Game to guess a random number
print("""Welcome to the guessing game
the number will be between 1-10""")

rand_answer = random.randint(1,10)
max_guesses = 4
guess_count = 0 
player_guess = 1
gameover = False

'''
while rand_answer != int(player_guess) and guess_count < max_guesses :
   
    player_guess = input("What is your guess? ")
    guess_count += 1
    if(int(player_guess) != rand_answer):
        print('Wrong answer, please guess again ' )
        player_guess = input("What is your guess? ")
        guess_count += 1
        print('Guess ' + str(guess_count) + ' of ' + str(max_guesses))
    elif(int(player_guess) == rand_answer):
        print('Correct guess')
        break   
    elif(guess_count == max_guesses):
        print("Your out of guesses ")
        break
'''
while True:
   
    player_guess = input("What is your guess? ")
    #guess_count += 1
    if(int(player_guess) != rand_answer):
        print('Wrong answer, please guess again ' )
        print("\n")
        #player_guess = input("What is your guess? ")
        guess_count += 1
        print('Yoour Guess ' + str(guess_count) + ' out of ' + str(max_guesses))
    elif(int(player_guess) == rand_answer):
        print('Correct guess')
        break   
    elif(guess_count == max_guesses):
        print("Your out of guesses ")
        break
print('random number is ' + str(rand_answer))
print('number guessed ' + str(player_guess))