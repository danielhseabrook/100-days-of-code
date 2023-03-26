from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
current_auction = {}
def auction_system(person_name, person_bid):
  current_auction[person_name] = person_bid


print(art.logo)
print("Welcome to the auction!")
other_people = "yes"
while other_people == "yes":
  person_name = input("What is your name?\n")
  person_bid = int(input("How much would you like to bid?\n"))
  auction_system(person_name, person_bid)
  other_people = input("Are there other people bidding today?\n")
  clear()
winner = max(current_auction, key=current_auction.get)

print(f"The winner is {winner} with a bid of ${current_auction[winner]}")
