"""Exercise 3 page 158.
Write a function called doubles()that takes a number as its input and doubles it. 
Then use doubles() in a loop to double the number 2 three times, displaying each result on a separate line. 
Here's some sample output: 4, 8, 16."""



def doubles(n):
    return n * 2

n2 = int(input("Enter a number: "))

for n in range(3):
    n2 = doubles(n2)
    print(n2)




"""Challenge 6.3 page 149: Convert Temperatures
   Write a program called temperature.py that defines two functions:
   1.convert_cel_to_far(), which takes one float parameter representing the same temperature in degrees Fahrenheit using the following formula:

   F = C * 9/5 + 32

   2.convert_far_to_cel(), which takes one float parameter representing degrees Fahrenheit and returns a float representing the same temperature in degress Celsius using the following formula:

   C = (F - 32) * 5/9

   The program should do the following:

   1. Prompt the user to enter a temperature in degrees Fahrenheit and then display the temperature onverted to Celsius
   2. Prompt the user to enter a temperature in degrees Celsius and then display the temperature converted to Fahrenheit
   3.Display all converted temperatures rounded to two decimal places"""



def convert_cel_to_far(C):
    """ Converts Celcius temperature to Fahrenheit"""
    F = C * 9/5 + 32
    return F

def convert_far_to_cel(F):
    """ Converts Fahrenheit temperature to Celcius"""
    C = (F - 32) * 5/9
    return C


C = input("Enter a temperature in degrees C: ")

F = convert_cel_to_far(float(C))

print(f"{C} degrees C = {F} degrees F")

F = input("Enter a temperature in degrees F: ")

C = convert_far_to_cel(float(F))

print(f"{F} degrees F = {C} degrees C")




"""Challenge 6.5
   In this challenge, you'll write a program called invest.py that tracks the growing amount of an investment over time.
   
   The initial deposit for an investment is called the principal amount. Each year, the amount increases by a fixed percentage, called the annual rate of return.
   
   For example, a principal amount of $100.00 with an annual rate of return of 5 percent increases the first year by $5.00 for a new amount of $105.00.
   The second year, the increase is 5 percent of $105.00, or $5.25, bringing the total to $110.25.
   
   Write a function called invest with three parameters: the principal amount, the annual rate of return, and the number of years to calculate.
   The function signature might look something like this:

   def invest(amount, rate, years):

   The function should then print out the amount of the investment, rounded to two decimal places, at the end of each year for the specified number of years.

   For example, calling invest(100, .05, 4) should print the following:
   year 1: $105.00
   year 2: $110.25
   year 3: $115.76
   year 4: $121.55

   To finish this program, prompt the user to enter an initial amount, an annual percentage rate, and a number of years.
   Then call invest() to display the calculations for the values entered by the user.
"""



def invest(amount, rate, years):
    """ Calculates savings after specified number of years """
    amount = amount + (amount * rate)
    return amount

amount = float(input("Enter principal amount of money: "))
years = int(input("Enter number of years: "))
rate = float(input("Enter annual rate of return: ")) 

for n in range(years):
    amount = amount + (amount * rate)
    print(f" year {n+1}: ${amount}")


