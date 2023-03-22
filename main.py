go_for_caesar = "yes"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)
#Defining the cypher tool
def caesar(text,shift):
#The encryption aspect of the cypher tool
  if direction == "encrypt":
    cypher = ""
    for letter in text:
      if letter in alphabet:
        position = alphabet.index(letter)
        encoded_position = int(position + shift)
        if encoded_position > 25:
          encoded_position = encoded_position % 26
        encoded_l = alphabet[encoded_position]
        cypher = cypher + encoded_l
      else:
        cypher = cypher + letter
    print(f"The encoded message is {cypher}")
#The decryption aspect of the cypher tool        
  elif direction == "decrypt":
    decrypted_text = ""
    for letter in text:
      if letter in text:
        position = alphabet.index(letter)
        decoded_position = int(position - shift)
        if decoded_position < 0:
          decoded_position = decoded_position % 26
        decoded_l = alphabet[decoded_position]
        decrypted_text = decrypted_text + decoded_l
      else:
        cypher = cypher + decrypted_text + letter
    print(f"The decoded message is {decrypted_text}")

#Function runs untill go_for_caesar changes state.
while go_for_caesar == "yes":
  direction = input("encrypt or decrypt? \n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
#Direction not 0 the cipher starts.  
  if direction != 0:
    caesar(text,shift)
  go_for_caesar = input("Would you like to restart the cipher program?\nyes or no?")