#DECRYPTION
#A Python Script that accepts a string as encrypted text and then the program will decrypt it using the following character substitute:
#'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !

#Ask the user to input an encrypted text
user_input = input("Please enter a string to decrypt: ")
#Check each character of the user's input
decrypted_output = ""
for i in range(len(user_input)):
    #If '*', change to 'a'
    if user_input[i] == "*":
        decrypted_output += "a"
    #If '&', change to 'e'
    elif user_input[i] == "&":
        decrypted_output += "e"
    #If '#', change to 'i'
    elif user_input[i] == "#":
        decrypted_output += "i"    
    #If '+', change to 'o'
    elif user_input[i] == "+":
        decrypted_output += "o"
    #If '!', change to 'u'
    elif user_input[i] == "!":
        decrypted_output += "u"
    else:
        decrypted_output += user_input[i]

#Print the output
print(decrypted_output)