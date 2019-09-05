# --------- ALGORTIHM ---------
# 1. Ask user to input a number
# 2. Assign the first input number to a variable defining it as the greatest number
# 3. Ask user to input another number
# 4. Compare the second number to the greatest number and define the greater number as the greatest number
# 5. Repeat steps three and four until user inputs a negative number
# 6. Print largest number
# --------- ALGORTIHM ---------

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = num_int
another_num_int = 0

while another_num_int >= 0:
    another_num_int = int(input("Input a number: "))
    if another_num_int > max_int:
        max_int = another_num_int

print("The maximum is", max_int)    # Do not change this line