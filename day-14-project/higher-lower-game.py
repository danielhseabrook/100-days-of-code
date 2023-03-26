import art
import game_data
import random
import os
# Generate a random choice from list for A
def subject_gen_a():
  global question_name_a
  global question_follower_count_a
  global question_descrption_a
  global question_country_a 
  a = random.randint(0, 49)
  name = list(map(lambda a : a['name'], game_data.data))
  follower_count = list(map(lambda a : a['follower_count'], game_data.data))
  description = list(map(lambda a : a['description'], game_data.data))
  country = list(map(lambda a : a['country'], game_data.data))
  question_name_a = name[a]
  question_follower_count_a = follower_count[a]
  question_descrption_a = description[a]
  question_country_a = country[a]
#Generate a random choice from list for B 
def subject_gen_b():
  global question_name_b
  global question_follower_count_b
  global question_descrption_b
  global question_country_b
  global question_name_a
  global last_b
  b = random.randint(0, 49)
  while b == last_b:
    b = random.randint(0,49)
  name = list(map(lambda b : b['name'], game_data.data))
  follower_count = list(map(lambda b : b['follower_count'], game_data.data))
  description = list(map(lambda b : b['description'], game_data.data))
  country = list(map(lambda b : b['country'], game_data.data))
  question_name_b = name[b]
  question_follower_count_b = follower_count[b]
  question_descrption_b = description[b]
  question_country_b = country[b]
  if question_name_b == question_name_a:
    subject_gen_b()
  last_b = b
#Compare A and B with answer. Shift B to A and regen appropriate slot depending on correct answer. returns correct/incorrect.
def compare_answer(answer):
  correct_answer = ""
  if question_follower_count_a > question_follower_count_b:
    correct_answer = "A"
    subject_gen_b()
  elif question_follower_count_b > question_follower_count_a:
    correct_answer = "B"
    swap_b_a()
    subject_gen_b()
  else:
    pass
  if answer == correct_answer:
    return "correct"
  else:
    return "incorrect"
#Swaps position B to position A in the case of B being correct.
def swap_b_a():
  global question_name_a
  global question_follower_count_a
  global question_descrption_a
  global question_country_a
  global question_name_b
  global question_follower_count_b
  global question_descrption_b
  global question_country_b
  question_name_a = question_name_b 
  question_follower_count_a = question_follower_count_b
  question_descrption_a = question_descrption_b
  question_country_a = question_country_b 

  
 ##########################################################################
##########################start game#######################################
############################################################################

# Replay loop to manage resetting variables
replay = ""
while replay != "N":
  question_name_a = ""
  question_follower_count_a = ""
  question_descrption_a = ""
  question_country_a = ""
  question_name_b = ""
  question_follower_count_b = ""
  question_descrption_b = ""
  question_country_b = ""
  last_b = ""
  score = 0
  playing = True
  subject_gen_a()
  subject_gen_b()
  #Game loop
  while playing:
    print(art.logo)
    #Present option A
    print(f"A:{question_name_a}, a {question_descrption_a} from {question_country_a}.")
    print(art.vs)
    #Present option B
    print(f"Against B:{question_name_b}, a {question_descrption_b} from {question_country_b}.")
    #Take answer as input for the question
    answer = input("Who has more followers? Type 'A' or 'B'\n")
    #call function to confirm answer
    question_result = compare_answer(answer)
    if question_result == "incorrect":
      playing = False
      replay = input(f"Incorrect!\nPlay again? Y/N\n")
      os.system('clear')
      continue
              
    elif question_result == "correct":
      score += 1
      os.system('clear')
      print(f"Correct! Your score is {score}.")
