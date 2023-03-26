import random
import os
logo = """                                                            
 .--.               .---.         .   .          .              
:                     | |         |\  |          |              
| --.  ..-..--.--.    | |--..-.   | \ .  ..--.--.|.-. .-..--.   
:   |  (.-'`--`--.    | |  (.-'   |  \|  ||  |  ||   (.-'|      
 `--`--``--`--`--'    ' '  ``--'  '   `--`'  '  `'`-' `--'      
"""
#select secret number
secret_number = random.randint(1,101)
numbers_guessed = []
#Set difficulty. E is 10 guesses, H is 5.
def difficulty():
  acceptable_answers = ["H","E"]
  guesses_left = 0
  local_choice = input("Would you like to play the game on \'E\'asy or \'H\'ard?\n")
  while local_choice not in acceptable_answers:
     local_choice = input("Please enter E for Easy or H for Hard.\n")
  if local_choice == "E":
      guesses_left = 10
  elif local_choice == "H":
      guesses_left = 5
  return guesses_left
################################################################
################# START GAME ###################################
################################################################
#Outerloop to manage variables for replay
replay = "yes"
while replay == "Y":
  os.system('clear')
  print(logo)
  guesses_left = difficulty()
  guess = "incorrect"
  #Game loop
  while int(guesses_left) > int(0) and guess == "incorrect":
    #Take guess input
    current_guess = int(input(f"You have {guesses_left} guesses left. Guess a number between 1 and 100\n"))
    #check if number has already been guessed
    while current_guess in numbers_guessed:
      print(f"Your guesses so far:\n{numbers_guessed}")
      current_guess = int(input(f"You have already guessed {current_guess}.\nPlease enter a number you have not tried\n"))
    numbers_guessed.append(current_guess)
    #compare current guess with secret number
    if secret_number > current_guess:
      print(f"The secret number is higher than {current_guess}")
      guesses_left -= 1
    elif secret_number < current_guess:
      print(f"The secret number is lower than {current_guess}")
      guesses_left -= 1
    elif secret_number == current_guess:
      guesses_left -= 1
      print(f"Correct! The secret number is {current_guess}.\nYou guessed correctly with {guesses_left} remaining.")
      guess = "correct"
    if guesses_left == 0:
      replay = input("You've run out of guesses.\nWould you like to play again? Y/N\n")
      numbers_guessed.clear()
    elif guess == "correct":
      replay = input("Would you like to play again? Y/N\n")
      numbers_guessed.clear()
