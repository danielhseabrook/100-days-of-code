import random
playing = "yes"
while playing == "yes":
  rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  '''
  
  paper = '''
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
  '''
  
  scissors = '''
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  '''
  player = "invalid"
  npc = random.randint(0,2)
  #Determining the NPC move
  if npc == 0:
    npc = "rock"
  elif npc == 1:
    npc = "paper"
  else:
    npc = "scissors"
  #Beggining game. Loops if invalid entry.  
  while player == "invalid":
    #Determining the players move and printing results.
    player = input("Rock, paper or scissors?\n")    
    print(f"You play\n{player}")    
    if player == "rock":
      print(rock)
    elif player == "paper":
      print(paper)
    elif player == "scissors":
      print(scissors)
    else:
      player = "invalid"
      continue
  #printing NPC results
  print(f"The computer plays\n{npc}")
  if npc == "rock":
    print(rock)
  elif npc == "paper":
    print(paper)
  elif player == "scissors":
    print(scissors)
  #determining the victor
  if player == "rock" and npc == "scissors":
    playing = input("You win!\nPlay again?")
    continue 
  elif player == "paper" and npc == "rock": 
    playing = input("You win!\nPlay again?")
    continue 
  elif player == "scissors" and npc == "paper":
    playing = input("You win!\nPlay again?")
    continue
    
  elif npc == "rock" and player == "scissors":
    playing = input("You lose!\nPlay again?")
    continue    
  elif npc == "paper" and player == "rock":
    playing = input("You lose!\nPlay again?")
    continue 
  elif npc == "scissors" and player == "paper":
    playing = input("You lose!\nPlay again?")
    continue
    
  elif player == npc:
    print("Draw!")
    playing = "yes"
    
  else:
    print("You typed an incorrect entry.\n You lose.")
    playing = "yes"
    continue
exit()
