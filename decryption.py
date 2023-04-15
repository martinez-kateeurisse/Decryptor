#Kate Eurisse Martinez_BSCPE 1-5_Decryption

#DECRYPTION
#A Python Script that accepts a string as encrypted text and then the program will decrypt it using the following character substitute:
#'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !

#Importing modules for the program's design and text formatting
import pyfiglet 
from colorama import Back, Fore, Style 

#Asking the user's name and printing a greeting
name = input("Enter your name: ")
print(("Hello ").center(84, "*"),"\n")

#Displaying the program's instructions
print("This program will decrypt your encrypted text using the following character substitute:")
char_eq = "'a' = *,  'e' = & , 'i' = #, 'o' = + ,'u' = !"
print(char_eq.center(85, " "), "\n")

#Using a while loop in case that the user wanted to decrypt another message
Retry = 'y'
while Retry == 'y':
    #Ask the user to input an encrypted text
    user_input = input("Please enter a string to decrypt: ")
    #Check each character of the user's input
    decrypted_output = "" #initializing output variable
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

    #Displaying the output with a design through the imported modules
    #Displaying the output
    print("The plain text of " + user_input, "is " )
    print(pyfiglet.figlet_format(decrypted_output, font = "block"))
    
    #Asking the user whether to decrypt another message or not
    Retry = input("Do you want to decrypt another message? (Please type 'y' if yes and any key if no): ")
    Retry = Retry.lower()

#Displaying thank you message    