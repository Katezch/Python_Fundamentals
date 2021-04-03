'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

use_number = int(input("Please enter a number between 0 and 1,000,000,000:"))

guess = 0

while guess != use_number:
    guess += 1

print(guess)