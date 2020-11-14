# imports
import sys


# Takes number string and creates list with each node of a predetermined length.
def infinite_num_build(digits, node_length):
    number_list = []
    i = 0
    node = ''
    for index in digits:
        if i % node_length == 0:
            if node != '':
                number_list.append(node)
            node = ''
        node += index
        i += 1
    number_list.append(node)
    return number_list


# Checks for correct inputs based on assignment
def limit_check(to_be_checked, function):
    node = 4
    input_length_limit = 40
    output_length_limit = 100
    length_limit = 0
    if function == 'node':
        if int(to_be_checked) > node:
            return 'invalid expression'
    else:
        if function == 'input':
            length_limit = input_length_limit
        elif function == 'output':
            length_limit = output_length_limit
        # Length check
        i = 0
        while i < len(to_be_checked):
            digit_length = 0
            while i < len(to_be_checked) and to_be_checked[i].isdigit():
                digit_length += 1
                i += 1
                if digit_length > length_limit:
                    return 'invalid expression'
            i += 1
        return to_be_checked


# Finds digit at specific index
def infinite_int_digit_index(number, index):
    count = 0
    for sublist in number:
        for digit in sublist:
            if count == index:
                return digit
            count += 1


# Counts number of digits in infinite int format number
def infinite_int_digit_count(number):
    count = 0
    for sublist in number:
        count += len(sublist)
    return count


# Iteratively adds two numbers built from lists.
def add(num1, num2, node_length):
    # Error Checking
    if num1 == 'invalid expression' or num2 == 'invalid expression':
        return 'invalid expression'

    answer = ''
    overflow = 0
    num1_length = infinite_int_digit_count(num1)
    num2_length = infinite_int_digit_count(num2)
    add_number_length = max(num1_length, num2_length)
    for i in range(add_number_length):
        if i >= num1_length:
            digit1 = 0
        else:
            digit1 = infinite_int_digit_index(num1, num1_length-1-i)
        if i >= num2_length:
            digit2 = 0
        else:
            digit2 = infinite_int_digit_index(num2, num2_length-1-i)
        added = int(digit1) + int(digit2) + overflow
        overflow = 0

        if added > 9:
            overflow = 1
            added -= 10

        answer = str(added) + answer
    if overflow > 0:
        answer = str(overflow) + answer
    answer_infinite_format = infinite_num_build(answer, node_length)
    return answer_infinite_format


# Function to multiply two numbers
def multiply(num1, num2, node_length):
    num1_length = infinite_int_digit_count(num1)
    num2_length = infinite_int_digit_count(num2)

    # Error Checking
    if num1 == 'invalid expression' or num2 == 'invalid expression':
        return 'invalid expression'
    if num1 == ['0'] or num2 == ['0']:
        return ['0']
    answer = infinite_num_build('0', node_length)

    for i in range(num1_length):
        for j in range(num2_length):
            digit1 = infinite_int_digit_index(num1, num1_length-i-1)
            # print('Digit 1: ' + str(digit1))
            digit2 = infinite_int_digit_index(num2, num2_length-j-1)
            # print('To be multiplied: {} * {}'.format(digit1, digit2))
            multiplied = str(int(digit1) * int(digit2)) + (i * '0') + (j * '0')
            # print(multiplied)
            multiplied_infinite_num = infinite_num_build(multiplied, node_length)
            answer = add(answer, multiplied_infinite_num, node_length)
            # print(answer)
    return answer


# Converts nested number list to string for printing
def list_print_to_string(list_to_print):
    answer_string = ''
    for sublist in list_to_print:
        for digit in sublist:
            answer_string += digit
    answer_string = limit_check(answer_string, 'output')
    return answer_string


# To solve nested operations, loosely based on evaluation expression examples on GeekForGeeks
def nested_operations(string_line, node_length):
    try:
        operation_stack = []
        digit_stack = []
        i = 0
        while i < len(string_line):
            operator = ''
            if string_line[i].isalpha():
                while i < len(string_line) and string_line[i].isalpha():
                    operator += string_line[i]
                    i += 1
                if string_line[i] == '(':
                    operation_stack.append(operator)
                    i += 1
            elif string_line[i].isdigit():
                digit = ''
                while i < len(string_line) and string_line[i].isdigit():
                    digit += string_line[i]
                    i += 1
                digit_stack.append(infinite_num_build(digit, node_length))
            elif string_line[i] == ')':
                operation = operation_stack.pop()
                if operation == 'multiply':
                    digit_stack.append(multiply(digit_stack.pop(), digit_stack.pop(), node_length))
                elif operation == 'add':
                    digit_stack.append(add(digit_stack.pop(), digit_stack.pop(), node_length))
                else:
                    return 'invalid expression'
                i += 1
            else:
                i += 1
        if len(digit_stack) != 1:
            return 'invalid expression'
        return limit_check(list_print_to_string(digit_stack.pop()), 'output')
    except:
        return 'invalid expression'


# Main function
# Check argument length
if len(sys.argv) < 2:
    print('Error: Insufficient filename arguments found')
    sys.exit()
arg1 = sys.argv[1]

fileName = ''
nodeLength = ''

# Separate file name from input argument
for ind in range(6, arg1.find(';')):
    fileName += arg1[ind]
# Separate node length from input argument
try:
    for ind in range(arg1.find(';') + 15, len(arg1)):
        nodeLength += arg1[ind]
    nodeLengthInt = int(nodeLength)
    if limit_check(nodeLengthInt, 'node') == 'invalid expression':
        print('Invalid node length')
        sys.exit()
except Exception:
    nodeLengthInt = 3

with open(fileName) as fp:
    for line in fp:
        line = line.rstrip('\n')
        if line != '':
            print(line, "=", nested_operations(limit_check(line, 'input'), nodeLengthInt), sep='')
