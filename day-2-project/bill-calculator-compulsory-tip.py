bill_amount = (input("How much was the bill?\n"))

if "$" in bill_amount:
  bill_amount = bill_amount.replace("$", "")  

n_people = int(input("How many people are we splitting the bill with today?\n"))
tip_amount = input("How much would everyone like to tip?\n")

if "%" in tip_amount:
  tip_amount = tip_amount.replace("%", "")

while int(tip_amount) < 10:
  tip_amount = input("Sorry, could you please repeat that?\n")

bill_amount = float(bill_amount)
tip_amount = float(tip_amount)
tip_percentage = float(tip_amount/100)
tip_value = float(tip_percentage*bill_amount)
bill_split = float((bill_amount+tip_value)/n_people)
print("Each person will pay(in dollars):")
print( "$" + "%.2f" % bill_split)
