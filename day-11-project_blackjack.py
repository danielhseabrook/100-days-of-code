import random
#Defining lists and variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
player_hand_split = []
dealer_hand = []
dealer_hand_split = []
person = ""
#Defining functions
#Draw cards to the set hand
def draw_card(hand):
  hand.append(random.choice(cards))
#Start game
def start_game(hand):
  draw_card(player_hand)
  draw_card(player_hand)
  draw_card(dealer_hand)
  draw_card(dealer_hand)
#Split hand
def split_hand(hand, split):
  hand[0] = split[0]
  hand.remove(0)
