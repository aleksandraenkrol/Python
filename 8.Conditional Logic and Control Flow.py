#Do you pass the class:

grade = 40

if grade >= 70:
    print("You passed the class!")

if grade < 70:
    print("You did not pass the class :( ")

print("Thank you for attending")

#or

grade = 40

if grade >= 70:
    print("You passed the class!")
else:
    print("You did not pass the class :( ")

print("Thank you for attending")




#Who wins the match?

sport = input("Enter a sport: ")
p1_score = int(input("Enter player 1 score: "))
p2_score = int(input("Enter player 2 score: "))


if p1_score == p2_score:
    print("The game is a draw.")

#1
elif sport.lower() == "basketball":

    if p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")

#2
elif sport.lower() == "golf":
    if p1_score < p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")

#3
else:
    print("Unknown sport")

# to simplify

""" Conditions:
sport = sport.lower()
p1_wins_bbal = (sport == "basketball") and (p1_score > p2_score)
p1_wins_golf = (sport == "golf") and (p1_score < p2_score)
p1_wins = player1_wins_basketball or player1_wins_golf
"""

sport = sport.lower()
if p1_score == p2_score:
    print("The game is a draw.")
elif (sport == "basketball") or (sport == "golf"):
    p1_wins_bbal = (sport == "basketball") and (p1_score > p2_score)
    p1_wins_golf = (sport == "golf") and (p1_score < p2_score)
    p1_wins = p1_wins_bbal or p1_wins_golf
    if p1_wins:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport")

    
#8.3 Exercise 1
"""Write a program that prompts the user to enter a word using the input() function and compares the lenght
of the word to the number five. The program should display one of the following outputs,
depending on the lenght of the user's input:
"Your input is less than 5 characters long"
"Your input is greater than 5 characters long"
"Your input is 5 characters long"
"""

word = input("Enter a word: ")

if len(word) < 5
    print("Your input is less than 5 characters long")
elif len(word) > 5
    print("Your input is greater than 5 characters long")
else:
    print("Your input is 5 characters long")


#8.3 Exercise 2
"""Write a program that displays "I'm thinking of a number between 1 and 10. Guess which one."
Then use input() to get a number from the user. If the used inputs the number 3, then the program should display "You win!".
For any other input, the program should display "You lose."
"""

print("I'm thinking of a number between 1 and 10. Guess which one.")

number = int(input())

if number == 3:
    print("You win!")
else:
    print("You lose.")


#8.4 Challenge: Find the Factors of a Number
"""
A factor of a positive integer n is any positive integer less than or equal to n that divides n with no remainder.
For example, 3 is a factor of 12 because 12 divided by 3 is 4 with no remainder. However, 5 is not a factor of 12
because 5 goes into 12 twice with a remainder of 2.

Write a program called factors.py that asks the user to input a positive integer and then prints out the factors of that number.
Here's a sample run of the program with output:

Enter a positive integer: 12
1 is a factor of 12
2 is a factor of 12
3 is a factor of 12
4 is a factor of 12
6 is a factor of 12
12 is a factor of 12

Hint: Recall from chapter 5 that you can use the % operator to get the remainder of dividing one number by another.
"""

num = int(input("Enter positive integer: "))

for factor in range(1, num+1):
    if num % factor == 0:
        print(f"{factor} is a factor of 12")


#8.5 Exercise 1
"""
Using break, write a program that repeatedly asks the user for some input and quits only if the user enters "q" or "Q". 
"""

text = input("Some text: ")
text = text.lower()

for character in text:
    if character == "q":
        break
else:
    print("There is no 'q' or 'Q' in this text")


#8.5 Exercise 2
"""
Using continue, write a program that loops over the numbers 1 to 50 and prints all numbers that are not multiples of 3. 
"""

for num in range(1, 51):
    if num % 3 == 0:
        continue
    print(num)


#8.6 Exercise 1
"""
Write a program that repeatedly asks the user to input an integer.
If the user enters something other than an integer, then the program should catch the ValueError and display the message "Try again". 
Once the user enters an integer, the program should display the number back to the user and end without crashing.
"""

number = 0

while number >= 0:
    try:
        number = int(input("Enter an integer: "))
        print(number)
        break
    except ValueError:
        print("Try again")


#8.6 Exercise 2
"""
Write a program that asks the user to input a string and an integer n, then display the character at index n in the string.
Use error handling to make sure the program doesn't crash if the user enters something other than an integer or if the index is out of bounds.
The program should display a different message depending on which error occurs.
"""

try:
    text = input("Write some text: ")
    num = int(input("Write an integer: "))
    character = text[num]

    print(character)
        
except ValueError:
    print("Entered value must be an integer")
    
except IndexError:
    print("Entered index is out of range")


# 8.7 Exercise 1
"""
Write a function called roll() that uses randint() to simulate rolling a fair die by returning a random integer between 1 and 6.
"""

from random import randint

def roll():
    """Return random integer between 1 and 6"""
    return randint(1, 6)

result = roll()
print(f"Result of rolling a fair die is {result}")


# 8.7 Exercise 2
"""
Write a program that simulates ten thousand rools of a fair die and displays the average number rolled.
"""

from random import randint

def roll():
    return randint(1, 6)

#Create a list of dice results
results = []

for trial in range(10_000):
    result = roll()
    results.append(result)

average = sum(results)/len(results)

print(f"Average: {average}")


# 8.8 Challenge: Simulate a Coin Toss Experiment
"""
Suppose you flip a fair coin repeatedly until it lands on heads and tails at least one time each.
In other words, after the first flip, you continue to flip the coin until it lands on the other side.

Doing this generates a sequence of heads and tails. For example, the first time you do this experiment,
the sequence might be heads, heads, tails.

On average, how many flips are needed for the sequence to contain both heads and tails?

Write simulation that runs ten thousand trials of the experiment and prints the average number of flips
per trial.
"""

import random

def coin_flip():
    """Randomly returns 'heads' or 'tails'."""

    return random.choice(['heads', 'tails'])


def generate_sequence():    
    """Generates a sequence of coin flips until both sides ('heads' and 'tails') are rolled at least once."""

    sequence = []
    
    while True:
        flip_result = coin_flip()
        sequence.append(flip_result)
        if 'heads' in sequence and 'tails' in sequence:
            break    
    return sequence

def average_flips_needed(trials):
    """Simulates the experiment in a specified number of trials, records the number of flips required for each trial, and calculates the average number of flips needed."""
    
    total_flips = 0

    for n in range(trials):
        sequence = generate_sequence()
        total_flips += len(sequence)
    return total_flips / trials

num_trials = 10_000
average_flips = average_flips_needed(num_trials)

print(f"On average, {average_flips:.2f} flips are needed to get both heads and tails in {num_trials} trials")
