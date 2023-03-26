import art
import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
player_hand_split = []
dealer_hand = []
####Defining functions
#Draw cards to the set hand
def draw_card(hand, handsum):
  card_choice = random.randint(0,12)
  if card_choice == 0 and handsum + 11 > 21:
    hand.append(1)
  else:
    hand.append(cards[card_choice])
#Dealer logic. CHeck if total current score is above 16. If above, draw
def dealer_logic():
  if dealer_hand_sum < 16:
    draw_card(dealer_hand, dealer_hand_sum)
  else:
    pass
#Start game
def start_game(player, dealer):
  draw_card(player_hand, player_hand_sum)
  draw_card(player_hand, player_hand_sum)
  draw_card(dealer_hand, dealer_hand_sum)
  draw_card(dealer_hand, dealer_hand_sum)  
#Show hands
def show_hands():
  print(f"Player\'s hand: {player_hand}")
  if  len(player_hand_split) > 0:
    print (f"Player\'s second hand: {player_hand_split}") 
  else:
    pass
  print(f"Dealer\'s hand: {dealer_hand[0]}")  
#Check hands
def check_hand_sum():
  global player_hand_sum
  global player_hand_split_sum
  global dealer_hand_sum
  player_hand_sum = sum(player_hand)
  player_hand_split_sum = sum(player_hand_split)
  dealer_hand_sum = sum(dealer_hand)
##########################################################
#Start game ##############################################
##########################################################
#Begin outerloop to manage resetting the game variables
replay = "yes"
while replay == "yes":
  os.system('clear')
  print(art.logo)
  player_hand.clear()
  player_hand_split.clear()
  dealer_hand.clear()
  player_status = ""
  dealer_status = ""
  person = ""
  player_hand_sum = 0
  player_hand_split_sum = 0
  dealer_hand_sum = 0
  start_game(player_hand, dealer_hand)
#Begin game loop
  game_status = ""
  while game_status == "":
  #Check for black jack from inital dealt cards
    check_hand_sum()
    if player_hand_sum == 21:
      game_status == "Win"
      print("Black jack!\nYou win!")
      print (f"Player\'s second hand: {player_hand_split} with a score of {player_hand_split_sum}")    
      print(f"Dealer\'s hand: {dealer_hand} with a score of {dealer_hand_sum}")
    elif dealer_hand_sum == 21:
      game_status == "lose"
      print("Dealer has black jack!\nYou lose.")
      print (f"Player\'s second hand: {player_hand_split} with a score of {player_hand_split_sum}")    
      print(f"Dealer\'s hand: {dealer_hand} with a score of {dealer_hand_sum}")
    show_hands()
    #Take player input for turn. Dealer logic runs after any input.  
    player_action = input("Would you like to \"Hit\", \"Split\", or \"Stay\"?\n")
    if player_action == "hit":
      #Check if the player has previously split hands and ask which to       play.
      if len(player_hand_split) > 0:
        hand_select = input("Play first or second hand?\n")
        if hand_select == "second":
          draw_card(player_hand_split, player_hand_split_sum) 
          dealer_logic()
        else:
          draw_card(player_hand, player_hand_split_sum)
          dealer_logic()
      else:
        draw_card(player_hand, player_hand_sum)
        dealer_logic()
    #If the player splits, append card in position [0] to position 0       in the player_hand_split list.
    elif player_action == "split":
      player_hand_split.append(player_hand.pop(0))
      dealer_logic()
    else:
      dealer_logic()
    check_hand_sum()
  
    #Check hand sums for win, lose, draw.  
    if player_hand_sum > 21:
      game_status = "lose"
    elif player_hand_split_sum > 21:
      game_status = "lose"
    elif player_hand_sum == 21: 
      game_status = "win"
    elif player_hand_split_sum == 21:
      game_status = "win"
    elif dealer_hand_sum  > 21:
      game_status = "win"
    elif dealer_hand_sum == 21:
      game_status = "lose"
    elif dealer_hand_sum == player_hand_sum: 
      game_status = "draw" 
    elif player_hand_split_sum == dealer_hand_sum:
      game_status = "draw"
    #If game status changes, print hands with unobscured dealer hand       and scores.
    if game_status == "win" or game_status == "draw" or game_status == "lose":
      print(f"Player\'s hand: {player_hand} with a score of {player_hand_sum}")
      if  len(player_hand_split) > 0:
        print (f"Player\'s second hand: {player_hand_split} with a score of {player_hand_split_sum}")    
      print(f"Dealer\'s hand: {dealer_hand} with a score of {dealer_hand_sum}")
      
  #Post game status and ask if player would like to play again.
  if game_status == "lose":
    replay = input("You lose!\nPlay again?\n")
  elif game_status == "win":
    replay = input("You win!\nPlay again?\n")
  elif game_status == "draw":
    replay = input("The game is a draw!\nPlay again?\n")
  else:
    #If game status doesn't change continue the while loop
    continue
