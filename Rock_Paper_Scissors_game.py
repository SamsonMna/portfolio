import os
import random
import re

def play_status():
  responses = ['Yes', 'No']
  while True:
    try:
      response = input("Do you wish to play? (yes or no) ")
      if response.lower() not in responses:
        raise ValueError("yes or no only")
      if response.lower() = 'yes':
        return True
      else:
        os.system('clear')
        print('Thank you')
        # i.e., if you respond with a no, the game clears the screen and exits the screen.
        exit()
    except ValueError as err:
      print(err) # Anything else other than yes or no will print an error message.

def play_moves():
  play = True
  while play:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')
    print("Rock, Paper, Scissors - Go!")
    
  user_input = input("Choose your weapon" '[R]ock, [P]aper, [S]cissors: ')
  if not re.match('[RrSsPp]', user_input):
    print("Please choose a letter: ")
    print( # the choices for the user to make)
    continue
  print(f'You chose: {user_choice}')

  choices = ['R', 'P', 'S']
  opp_choice = random.choice(choices)
  
  print(f'I chose: {opp_choice}')
  
  if opp_choice == user_choice.upper():
    print("Tie!")
    play = check_play_status()
  elif opp_choice == 'R' and user_choice.upper() == 'P':
    print("Rock beats paper")
    play = check_play_status()
    
  elif opp_choice == 'S' and user_choice.upper() == 'P':
    print("Scissors beats paper!")
    play = check_play_status()
  
  elif opp_choice == 'P' and user_choice == 'R':
    print("paper beats rock!")
    play = check_play_status()
  else:
    print("You win!\n")
    play = check_play_status()
    
if __name__ == '__main__'
  play_moves
   
  
  
  
  
  
  
  
  
