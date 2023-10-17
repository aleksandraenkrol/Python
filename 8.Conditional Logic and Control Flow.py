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

