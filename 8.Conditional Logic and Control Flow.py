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
