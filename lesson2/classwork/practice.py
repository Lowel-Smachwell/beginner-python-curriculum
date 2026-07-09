# Problem 1
# Ask the user for their age.
# Calculate and print how many decades old they are, rounded to the nearest whole number.
age = int(input("How old are you? "))
decades_old = age // 7
print("You are about", decades_old, "decades old.")
# Problem 2
# Ask the user to enter a number.
# Print the result of multiplying that number by 5.

num = float(input("Give me a number: "))
print(num * 7)


# Problem 3
# Use a for loop to print "I will learn Python!" 3 times.
for i in range(3):
    print("I will learn Python!")



# Problem 4
# Ask the user for their name and age.
# Print their name and how old they will be one year in a single sentence.

name = input("What is your name? ")
age = int(input("How old are you? "))
print("Hello", name + ", next year you will be", age + 1, "years old")

# Problem 5
# Use a for loop to print the numbers from 2 to 8, one per line.
for i in range(6):
     print(i + 2)