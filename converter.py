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

if output_base_choice == "0" or output_base_choice == "binary":
	output_base_descriptor = "binary"
elif output_base_choice == "1" or output_base_choice == "hexadecimal":
	output_base_descriptor = "hexadecimal"
elif output_base_choice == "2" or output_base_choice == "decimal":
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
    
#CONVERTS USER INPUT INTO ALL UPPPERCASE
input_value = input_value.upper()

#SCRIPTS TO CALCULATE OUTPUTS
#converts any inputs into decimal first

if input_base_descriptor == "decimal":
    decimal_output = input_value

elif input_base_descriptor == "binary":
    rev_string(input_value)
    bi_to_dec_list = []
    power = 1
    current_digit = 0
    for i in range(len(input_value)): #repeats this for each digit in the input
        sub_output = int(reversed_string[current_digit]) * power
        bi_to_dec_list.append(sub_output)

        power *= 2
        current_digit += 1
    decimal_output = sum(bi_to_dec_list)

elif input_base_descriptor == "hexadecimal":
    power = len(input_value)
    decimal_output = 0
    hex_dec_dict = {
        "0" : "0",
        "1" : "1",
        "2" : "2",
        "3" : "3",
        "4" : "4",
        "5" : "5",
        "6" : "6",
        "7" : "7",
        "8" : "8",
        "9" : "9",
        "A" : "10",
        "B" : "11",
        "C" : "12",
        "D" : "13",
        "E" : "14",
        "F" : "15"
    }
    for i in input_value:
        power -= 1
        decimal_output += int(hex_dec_dict[str(i)]) * (16 ** power)


#converts decimal into desired output

if output_base_descriptor == "decimal":
    final_output = decimal_output

elif output_base_descriptor == "binary":
    #doesn't work for some reason
    '''
    def dec_to_binary(dec_input):
        global final_output
        if dec_input >= 1:
            dec_to_binary(dec_input // 2)
        final_output = dec_input % 2
        return final_output
    dec_to_binary(decimal_output)
    '''
    final_output = int(bin(int(decimal_output))[2:])

elif output_base_descriptor == "hexadecimal":
    power = 0
    final_output = 0
    dec_hex_list = {
        "0" : "0",
        "1" : "1",
        "2" : "2",
        "3" : "3",
        "4" : "4",
        "5" : "5",
        "6" : "6",
        "7" : "7",
        "8" : "8",
        "9" : "9",
        "10" : "A",
        "11" : "B",
        "12" : "C",
        "13" : "D",
        "14" : "E",
        "15" : "F"
    }
    #for i in decimal_output:
        #power += 1
        #final_output -= str(dec_hex_list[str(i)]) * (16 // power)

    final_output = str(hex(int(decimal_output))[2:])

#DESIRED OUTPUT PRINT
print(f"The {output_base_descriptor} representation of {input_value} ({input_base_descriptor}) is {final_output}")
