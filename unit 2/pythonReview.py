# create a new document called pythonReview.py and answer the following
# questions. 

# Question 1
# Build a program that determines if a student has submitted their class work 
# and homework assignment. The program should use an operator that allows 
# for evaluating 2 conditions and determining if the conditions are true 
# or false.

classwork_submitted = input("Did you submit your classwork? (yes/no): ").strip().lower()
homework_submitted = input("Did you submit your homework? (yes/no): ").strip().lower()

# Using the 'and' operator to check if both are true
if classwork_submitted == "yes" and homework_submitted == "yes":
print("Good job! You submitted both assignments.")
else:
print("You still have work to do!")

print() # just adds a blank line between questions

# hint: find the a operator that allows you to evaluate 2 condtions.

# Question 2
# Create a function that will take in a string as an argument and output 
# that string in reverse order.

def reverse_string(text):
reversed_text = text[::-1] # this reverses the string
return reversed_text

word = input("Enter a word to reverse: ")
print("Reversed word:", reverse_string(word))

print()




# hint: look into string reverse in w3schools

# Question 3
# Create a number guessing function where the program will continuously 
# ask the user to enter a number until the guess the number correctly. 
# Your program should also give the user information on if their guess 
# is close to the correct number. If the guess is above the correct number 
# it should tell the user it is too high and try again. 
# If the guess is below the number, it should tell the user it is too low, 
# it should tell them it is too low and to guess again. Once the user gets 
# it correct the program should congratulate them, stop, and tell them how 
# many attempts they made.

import random

def guess_number():
correct_number = random.randint(1, 10)
attempts = 0
guess = None

while guess != correct_number:
user_input = input("Guess a number between 1 and 10: ")

# make sure the input is a number
if not user_input.isdigit():
print("Please enter a valid number.")
continue

guess = int(user_input)
attempts += 1

if guess > correct_number:
print("Too high! Try again.")
elif guess < correct_number:
print("Too low! Try again.")
else:
print(f"Congratulations! You guessed it in {attempts} tries.")

guess_number()