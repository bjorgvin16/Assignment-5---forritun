# --------- ALGORTIHM ---------
# 1. First three numbers in sequence are 1, 2, and 3.
# 2. For fourth number in sequnce, add previous three numbers. 
#    For fifth number in sequence, add previous three numbers and so on. 
# 3. Ask user for an input n determining how many numbers from the sequnce, the program should print.
# 4. Print first three numbers of sequence outside of loop
# 4. Create a loop that:
#       Prints each number of the sequence except first three numbers
#       Changes the variables for the previous 3 numbers each loop
#       Adds previous three numbers each loop to find next number in sequence
#       Stops when n many numbers of sequence have been printed
# --------- ALGORTIHM ---------

n = int(input("Enter the length of the sequence: ")) # Do not change this line
first_num = 1
second_num = 2
third_num = 3

print(first_num)
print(second_num)
print(third_num)

counter = 3 # counter starts at 3 because first three numbers of sequencd have already been defined

while counter <= n:
    current_num = first_num + second_num + third_num
    print(current_num)
    first_num = second_num
    second_num = third_num
    third_num = current_num

    counter += 1
