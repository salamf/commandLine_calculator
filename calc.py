#!/usr/bin/python3


# Salam Fazil


import sys


# Adds 2 digit strings
def add(num1, num2):
    return int(num1) + int(num2)


# Multiplies 2 digit strings
def multiply(num1, num2):
    return int(num1) * int(num2)


# Replaces all instances of command in arg_str, with the computed result
# of the command.
# For example, lets say arg_str is (add 3 (multiply 3 3)).
# So the first command to compute here is (multiply 3 3).
# the result for this command is 9. By replacing (multiply 3 3) with 9,
# this function will return "(add 3 9)"
def replace_command(result, command, arg_str):
    if command in arg_str:
        return arg_str.replace(command, str(result))

    raise Exception("Something went wrong")


# Given a valid command argument, this function removes the useless
# parentheses around the arg.
# For example, lets say the command is (add 3 4).
# Here the args are 3 and 4. However, the way I have my program get the
# args, 4 will be 4) instead of 4. So this function will remove the ')'
# and return 4.
def remove_arg_parentheses(arg):
    if '(' in arg:
        return arg[1:]

    if ')' in arg:
        return arg[:len(arg) - 1]

    return arg


# Computes the given command and returns the result
def compute_command(command):
    word = command.split()[0]
    arg1 = remove_arg_parentheses(command.split()[1])
    arg2 = remove_arg_parentheses(command.split()[2])

    if word == "(add":
        return add(arg1, arg2)
    elif word == "(multiply":
        return multiply(arg1, arg2)
    else:
        raise Exception("Could not recognize command")


# This function check if the ARGS of a command are valid and can be used
# to compute the command
def check_args(command):
    arg1 = remove_arg_parentheses(command.split()[1])
    arg2 = remove_arg_parentheses(command.split()[2])

    if not arg1.isdigit() and not arg2.isdigit():
        raise Exception("Both of the args of the command {} are invalid"
                        .format(command))

    if not arg1.isdigit():
        raise Exception("The first arg of the command {} is invalid"
                        .format(command))

    if not arg2.isdigit():
        raise Exception("The second arg of the command {} is invalid"
                        .format(command))


# This function checks to make sure the given command is valid and
# can be computed.
def check_command(command):
    if command == "":
        raise Exception("Invalid command line arg")

    if len(command.split()) < 3:
        raise Exception("Not enough args in command {}"
                        .format(command))

    if len(command.split()) > 3:
        raise Exception("Too much args in command {}"
                        .format(command))

    check_args(command)  # The command is valid, now check if args are too


# This function finds the next command to be executed
# the next command to be executed will be the innermost command in between
# parentheses.
# For example: (multiply (add 3 4) 6)
# in the example above, the next command will be (add 3 4).
def get_next_command(arg_str):
    command = ""

    temp_str = ""
    for letter in arg_str:
        if letter == '(':
            temp_str = ""
        elif letter == ')':
            temp_str += letter
            command = temp_str
            break

        temp_str += letter

    # Check if the command is valid before returning it
    check_command(command)

    return command


def main():
    # Split the array of args given in the command line args by spaces
    # and store it into a string
    arg_str = ' '.join(sys.argv[1:])

    # if the given argument is a single digit, print it as an integer,
    # then stop program (return out of main function)
    if arg_str.isdigit():
        print(int(arg_str))
        return

    # This loop:
    #   1. Gets next command to be executed from the arg_str created
    #       (will be inner-most expression between parentheses)
    #   2. Computes the command and stores the answer in "result"
    #   3. Replaces all instances of the command in arg_str with the
    #       computed result
    #   4. Repeats until arg_str is a digit (all commands have been
    #       computed and replaced by their answers and we are left with
    #       the final answer)
    while True:
        command = get_next_command(arg_str)  # Gets next command
        result = compute_command(command)  # Computes the command
        arg_str = replace_command(result, command, arg_str)  # Replaces

        if arg_str.isdigit():  # Break out of loop when we have the answer
            break

    print(int(arg_str))  # Print result as an integer


if __name__ == "__main__":
    main()
