#BINARY TO INTEGER/NUMBER/DECIMAL CONVERTER
#this is just a test file to see if it'll work in the main converter.py file

binary_input = input("Please enter your binary input, no spaces: ")

power_2 = 1
current_digit = 0

binary_list = []
reversed_string_list = []

#reverses the string of binary digits
index_num = len(binary_input)
while index_num > 0:
    reversed_string_list += binary_input[index_num - 1]
    index_num -= 1
reversed_binary_string = "".join(reversed_string_list)

for i in range(len(binary_input)):
    sub_output = int(reversed_binary_string[current_digit]) * power_2
    binary_list.append(sub_output)

    power_2 *= 2
    current_digit += 1

final_output = sum(binary_list)
print(f"The decimal output to your binary input is {final_output}")