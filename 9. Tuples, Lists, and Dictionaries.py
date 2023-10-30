# 9.1 Exercise 1
"""
Create a tuple literal named cardinal_numbers that holds the strings "first", "second",
and "third", in that order.
"""

cardinal_numbers = ("first", "second", "third")

# 9.1 Exercise 2
"""
Using index notation and print(), display the string at index 1 in cardinal_numbers.
"""

print(cardinal_numbers[1])

# 9.1 Exercise 3
"""
In a single line of code, unpack the values in cardinal_numbers into three strings names
position1, position2, and position3. Then print each value on a separate line.
"""

position1, position2, position3 = cardinal_numbers

print(position1)
print(position2)
print(position3)

# 9.1 Exercise 4
"""
Using tuple() and a string literal, create a tuple called my_name that contains the letters 
of your  name.
"""

my_name = tuple("Aleksandra")

# 9.1 Exercise 5
"""
Check whether the character "x" is in my_name using the in keyword.
"""

"x" in my_name

# 9.1 Exercise 6
"""
Create a new tuple containing all but the first letter in my_name using slice notation.
"""

new_tuple = my_name[1:]

# 9.2 Exercise 1
"""
Create a list named food with two elements, "rice" and "beans".
"""

food = ["rice", "beans"]

# 9.2 Exercise 2
"""
Append the string "broccoli" to food using.append()
"""
food.append("broccoli")

# 9.2 Exercise 3
"""
Add the strings "bread" and "pizza" to food using.extend().
"""
food.extend(["bread", "pizza"])

# 9.2 Exercise 4
"""
Print the first two items in the food list using print() and slice notation.
"""
print(food[0:2])

# 9.2 Exercise 5
"""
Print the last item in food list using print() and index notation.
"""
print(food[-1])

# 9.2 Exercise 6
"""
Create a lost called breakfast from the string "eggs, fruit, orange juice" using the string.split() method.
"""
str = "eggs, fruit, orange juice"
breakfast = str.split(", ")

# 9.2 Exercise 7
"""
Verify that breakfast has three items using len().
"""
len(breakfast)

# 9.2 Exercise 8
"""
Create a new list called lengths using a list comprehension that contains the lengths of each string in the breakfast list.
"""
lengths = [len(word) for word in breakfast]

# 9.3 Exercise 1
"""
Create a tuple called data with two values. The first value should be the tuple (1, 2),
and the second value should be the tuple (3, 4).
"""
data = ((1, 2),(3, 4))

# 9.3 Exercise 2
"""
Write a for loop that loops over data and prints the sum of each nested tuple.
The output should look like this:
Row 1 sum: 3
Row 2 sum: 7
"""

for i, row in enumerate(data, 1):
    row_sum = sum(row)
    print(f"Row {i} sum: {row_sum}")

# 9.3 Exercise 3
"""
Create a list [4, 3, 2, 1] and assign it to the variable numbers.
"""

numbers = list((4, 3, 2, 1))

# Exercise 4
"""
Create a copy of the numbers list using the [:] slice notation.
"""

numbers1 = numbers[:]

# Exercise 5
"""
Sort the numbers list in numerical order using .sort(). 
"""

numbers1.sort()


# 9.4 Challenge: List of Lists
"""
Write a program that contains the following list of lists:

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
    ]

Define a function, enrollment_stats(), with a single parameter. This parameter should be a list of lists in which each individual list contains three elements:

1. The name of a university
2. The total number of enrolled students
3. The annual tuition fees

enrollment_stats() should return two lists, the first containing all the student enrollment values and the second containing all the tuition fees.

Next, define two functions, mean() and median(), that take a single list argument and return the mean or median of the values in each list, respectively.

Using universities, enrollment_status(), mean(), and median(), calculate the total number of students, the total tuition, the mean and median numbers of students, and the mean and
median tuition values.

Finally, output all values and format the output so that it looks like this:

****************************
Total students: 77,285
Total tuition: $271,905

Student mean: 11,040.71
Student median: 10,566

Tuition mean: $38,843.57
Tuition median: $39,849
****************************
"""

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
    ]

def enrollment_stats(university_data):
    """Returns three lists containing data about names of the universities, enrollment values and all the tuition fees"""
    name = []
    students = []
    fees = []

    for university in university_data:
        name.append(university[0])
        students.append(university[1])
        fees.append(university[2])

    return name, students, fees

name, students, fees = enrollment_stats(universities)

print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(fees):,}")

def mean(number_of_students):
    result = sum(number_of_students) / len(number_of_students)
    return result

print(f"Student mean: {mean(students):,.2f}")

def median(number_of_students):
    number_of_students.sort()

    lenght_of_list = len(students)

    if len(number_of_students) % 2 == 0:
        n = lenght_of_list / 2
        return ((number_of_students[n-1]+number_of_students[n+1])/2)
    else:
        return number_of_students[int((lenght_of_list)/2)]

print(f"Student median: {median(students):,}")

print(f"Tuition mean: {mean(fees):,.2f}")
print(f"Tuition median: $ {median(fees):,}")

# 9.5 Challenge: Wax Poetic
"""
In this challenge, you'll write a program that generates poetry.

Create five lists for different word types:

1. Nouns: ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
2. Verbs: ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
3. Adjectives: ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
4. Prepositions:["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
5. Adverbs: ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

Randomly select the following number of elements from each list:
-Three nouns
-Three verbs
-Three adjectives
-Two prepositions
-One adverb

You can do this with the choice() function in the random module. This function takes a list as input
and returns a randomly selected element of the list.

For example, here's how you use random.choice() to get random element from the list["a", "b", "c"]:

import random

random_element = random.choice(["a", "b", "c"])

Using the randomly selected words, generate and display a peom with the following structure inspired
by Cliffors Pickover:

{A/An}{adj1}{noun1}
{A/An}{adj1}{noun1}{verb1}{prep1}the{adj2}{noun2}
{adverb1},the{noun1}{verb2}
the {noun2}{verb3}{prep2}{a/an}{adj3}{noun3}

Here, adj stands for adjective and prep for preposition.

Here's an example of the kind of poem your program might generate:

A furry horse
A furry horse curdles within the fragrant mango
extravagantly, the horse slurps
the mango meows beneath a balding extrovert

Each time your program runs, it should generate a new poem.
"""
import random

Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]

Verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]

Adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]

Prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]

Adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

noun1 = random.choice(Nouns)
noun2 = random.choice(Nouns)
noun3 = random.choice(Nouns)

verb1 = random.choice(Verbs)
verb2 = random.choice(Verbs)
verb3 = random.choice(Verbs)

adj1 = random.choice(Adjectives)
adj2 = random.choice(Adjectives)
adj3 = random.choice(Adjectives)

prep1 = random.choice(Prepositions)
prep2 = random.choice(Prepositions)

adverb1 = random.choice(Adverbs)


print(f"A/An {adj1} {noun1}")
print(f"A/An {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}")
print(f"{adverb1}, the {noun1} {verb2}")
print(f"the {noun2} {verb3} {prep2} a/an {adj3} {noun3}")
