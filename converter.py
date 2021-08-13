'''
This program converts numbers between
the three primary representations used
in computer science: decimal (base 10),
binary (base 2), and hexidecimal 
(base 16).
'''
import time

#intro
print("BASE CONVERTER")
print("INPUT BASE\n")
print("[0] binary (Base 2)")
print("[1] hexadecimal (Base 16)")
print("[2] decimal (Base 10)")

#USER INPUT & BASE TYPE CHOICE
input_base_choice = input("\nWhat is the base of your input? ")
if input_base_choice == 0 or input_base_choice == "binary":
	input_base_descriptor = "binary"
elif input_base_choice == 1 or input_base_choice == "hexadecimal":
	input_base_descriptor = "hexadecimal"
elif input_base_choice == 2 or input_base_choice == "decimal":
	input_base_descriptor = "decimal"
else:
    print("Please enter a valid input!\nExiting in 3 seconds...")
    time.sleep(3)
    exit()

#ASKS FOR INTEGER INPUT
input_value = input(f"Enter a valid {input_base_descriptor}: ")

#ASKS FOR OUTPUT TYPE
print("\nOUTPUT BASE")
print("[0] binary (base 2)")
print("[1] hexadecimal (base 16)")
print("[2] decimal (base 10)\n")
output_base_choice = input("What base would you like to convert to? ")

if output_base_choice == 0 or output_base_choice == "binary":
	output_base_descriptor = "binary"
elif output_base_choice == 1 or output_base_choice == "hexadecimal":
	output_base_descriptor = "hexadecimal"
elif output_base_choice == 2 or output_base_choice == "decimal":
	output_base_descriptor = "decimal"
else:
    print("Please enter a valid input!\nExiting in 3 seconds...")
    time.sleep(3)
    exit()

#DEFINE FUNCTIONS
#reverses a string (aka test -> tset)
def rev_string(reverse_input):
    global reversed_string
    reversed_string_list = []
    index_num = len(reverse_input)
    while index_num > 0:
        reversed_string_list += reverse_input[index_num - 1]
        index_num -= 1
    reversed_string = "".join(reversed_string_list)
    

#SCRIPTS TO CALCULATE OUTPUTS
#converts any inputs into decimal first
rev_string(input_value)

if output_base_descriptor == "decimal":
    calc_output = input_value
elif output_base_descriptor == "binary":
    bi_to_dec_list = []
    power_two = 1
    current_digit = 0
    for i in range(len(input_value)): #repeats this for each digit in the input
        sub_output = int(reversed_string[current_digit]) * power_two
        bi_to_dec_list.append(sub_output)

        power_two *= 2
        current_digit += 1
    test = sum(bi_to_dec_list)
    print(test)



#DETERMINES WHICH CONVERT METHOD TO USE


'''
output_value = "***"
print("\nThe " + input_base_descriptor + " number " + input_value +
      " is equivalent to the " + output_base_descriptor + " number " +
      output_value)
'''