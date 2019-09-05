# --------- ALGORTIHM ---------
# 1. Ask user to input a number
# 2. Assign the first input number to a variable defining it as the greatest number
# 3. Ask user to input another number
# 4. Compare the second number to the greatest number and define the greater number as the greatest number
# 4. Repeat steps three and four until user inputs a negative number
# 5. Print largest number
# --------- ALGORTIHM ---------

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
num_int2 = int(input("Input another number: "))
max_int = 0

while num_int:
    if num_int >= num_int2:
        greatest_num = num_int
    else:
        greatest_num = num_int2

print("The maximum is", max_int)    # Do not change this line