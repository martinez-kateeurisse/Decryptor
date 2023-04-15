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
    else:
        decrypted_output += user_input[i]

#If '#', change to 'i'
#If '+', change to 'o'
#If '!', change to 'u'

#Print the output
print(decrypted_output)