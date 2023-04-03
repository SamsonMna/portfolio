# Number Guessing game
import random


rand_attempts = []
def show_score():
    if not  rand_attempts:
        print("0 highs score, Make one!")
    else:
        print(f"Current high score is {min\(rand_attempts\)} attempts")

def start_game():
    attempts = 0
    rand_num = random.randint(1, 10)
    print("Hello Gambler! Welcome to the number guessing game!")
    Gambler_name = input("What is your namr sir? ")
    wanna_play = input(f'Hi, {Gambler_name}, would you like to play?' "(Enter Yes/No): ")
    if wanna_play.lower() != 'yes':
        print("That\'s cool, Thanks!")
        exit()
    else:
        show_score()
    
    while wanna_play.lower() == 'yes':
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                raise ValueError("Guess a number between 1 and 10!")
            attempts = += 1
            rand_attempts.append(attempts)
            
            if guess = rand_num:
                print("Bam! You nailed it!")
                print(f'It took you {attempts} guesses')
                wanna_play = input("Would you like to play again? (Enter yes/no): ")
                if wanna_play.lower() != 'yes':
                    print("Cool, you do you...")
                    break
                else:
                    attemps = 0
                    rand_num = random.randint(1, 10)
                    show_score()
                    continue
    
        else:
            if guess > rand_num:
                print('It\'s lower')
            elif guess < rand_num:
                print("It\'s higher")
    except ValueError as err:
    print("Oh no!, not a valid number. Here is another free try for you...")
    print(err)
    
if __name__ == '__main__":
    start_game


            
            
            
            
            
            
            
            
            
            
