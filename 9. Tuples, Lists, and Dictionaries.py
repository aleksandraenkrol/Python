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
