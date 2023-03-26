import art

def multiply(first_number, second_number):
  return first_number * second_number

def add(first_number, second_number):
  return first_number + second_number

def subtract(first_number, second_number):
  return first_number - second_number

def divide(first_number, second_number):
  return first_number / second_number

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
  } 
def calculator():
  print(art.logo)
  continue_using = True
  first_number = 0
  while continue_using:
    if first_number == 0:
      first_number = float(input("What is the first number?\n")) 
    for symbol in operations:
      print(symbol)
    math_function = input("what is the mathematical function you would like to use?\n")
    second_number = float(input("What is the next number?\n"))    
    
    function = operations[math_function]
    answer = function(first_number, second_number)  
    
    print(f"{first_number} {math_function} {second_number} = {answer}")
    continue_ans = (input(f"Enter c to continue calculating with {answer}, n to begin new calculation or e to exit\n"))
    if continue_ans == "c":
      first_number = answer
      continue
    elif continue_ans == "n":
      calculator()
    else:
      exit()
calculator()
    


