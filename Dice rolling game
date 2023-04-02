# Lets roll some dies
import random
import os

def num_die():
    while True:
        try:
            num_die = input("Number of dice: ")
            valid_responses = ['1', 'one', '2', 'two']
            if num_die not in valid_responses:
                raise ValueError("Can only be one or two")
            else:
                return num_die
        except ValueError as err:
            print(err)
            
            
def rolling():
    min_value = 1
    max_value = 6
    roll_again = 'y'
    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        number = num_die()

        if number == '2' or number == 'two':
            print('Rolling the rice...')
            dice1 = random.randint(min_value, max_value)
            dice2 = random.randint(min_value, max_value)
            
            print('The values are: ')
            print('Dice one: ' dice1)
            print('Dice two: ' dice2)
            print('Total: ' dice1 + dice2)
            
            roll_again = input('Wanna go? ')
        else:
            print('Rolling... ') # I don't wanna know know... - Adam Lavine 🙃
            dice1 = random.randint(min_value, max_value)
            print(f'The value is: {dice1}')
            
            roll_again =  input("Wanna roll? ")
            
            
if __name__ == '__main__':
    rolling
            
            
            
            
            
            
            
            
            
            
