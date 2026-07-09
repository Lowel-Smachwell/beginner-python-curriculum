num_str = "42"
# "42" -> 42
# num_value + int(num_str)
print(num_str + "1")

decimal_str = "3.14"
# "3.14" -> 3.14
decimal_value = float(decimal_str)
print(decimal_value + 2.19)

# "16" not 16
age_text = input("How old are you ")
age = int(age_text)
print('Next year you will be', age + 1, "years old.")

num = 100
# 100 -> "100"
num_str2 = str(num)
print("This burger cost $" + num_str2)
