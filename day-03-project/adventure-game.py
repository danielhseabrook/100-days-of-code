print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
playing = "yes"
while playing == "yes":

  print("Welcome to Treasure Island.")
  print("Your mission is to find the treasure.") 
  
  
  current_position = 0
  
  current_position = input("You arrive at a crossraods. Do you go left or right?\n")
  current_position= current_position.lower()
  
  if current_position != "left":
    playing = input("You fall into a hole.\nGame Over\nPlay Again?\n")
    continue
  
  current_position = input("It begins to rain and the river bed in the distance starts to rapidly fill. Do you \"Swim\" across or \"wait\" for the storm to pass?\n")
  current_position= current_position.lower()
  
  if current_position != "wait":
    playing = input("You are taken in the violent current and drown.\nGame over.\nPlay Again?\n")
    continue
  
  current_position = input("You come to doors which are the colour of the rainbow.\n Which door will you pick?\n")
  current_position= current_position.lower()
  
  door_colours = ["red","orange","yellow","green","blue","indigo","violet"]
  
  while current_position not in door_colours:
    current_position = input("That colour is not a colour in the rainbow.\n Pick again.\n")
    current_position = current_position.lower()
  
  if current_position == "red":
    playing = input("You've been burnt alive.\nGame Over.\nPlay Again?\n")
    continue
  
  elif current_position == "blue":
    playing = input("You've been eaten by beats.\nGame Over.\nPlay Again?")
    continue
  
  elif current_position == "yellow":
    playing = input("You win!\nPlay Again?")
    continue
  
  else:
    playing = input("Game Over.\Play Again?\n")
exit()
