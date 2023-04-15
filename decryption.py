#Kate Eurisse Martinez_BSCPE 1-5_Decryption

#DECRYPTION
#A Python Script that accepts a string as encrypted text and then the program will decrypt it using the following character substitute:
#'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !

#Importing modules for the program's design and text formatting
import pyfiglet 
from colorama import Back, Fore, Style 

#Asking the user's name and printing a greeting
print("//" * 20)
name = input(f"{Fore.RED} Enter your name: "+ Fore.RESET)
print("//"*20, "\n\n") 
print(Back.LIGHTBLACK_EX, Fore.LIGHTCYAN_EX, ("Hello " + name).center(84, "*") + Back.RESET, "\n")

#Displaying the program's instructions
print(f"{Fore.GREEN}This program will decrypt your encrypted text using the following character substitute:")
char_eq = "'a' = *,  'e' = & , 'i' = #, 'o' = + ,'u' = !"
print(char_eq.center(85, " "), "\n")

#Using a while loop in case that the user wanted to decrypt another message
Retry = 'y'
while Retry == 'y':
    #Ask the user to input an encrypted text
    user_input = input(f"{Fore.RED}Please enter a string to decrypt: " + Fore.RESET)
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
    print(f"{Fore.BLUE}The plain text of ", ('\033[91m' + user_input), '\033[94m' + "is:" + "\n")
    print(Fore.MAGENTA,Style.BRIGHT,pyfiglet.figlet_format(decrypted_output, font = "block"))
    
    #Asking the user whether to decrypt another message or not
    Retry = input(f"{Fore.GREEN}\n\n\nDo you want to decrypt another message? (Please type 'y' if yes and any key if no): ")
    Retry = Retry.lower()

#Displaying thank you message    