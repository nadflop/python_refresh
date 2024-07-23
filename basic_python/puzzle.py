#!/usr/bin/python3
# based on https://www.w3resource.com/python-exercises/puzzles/index.php

# exercise done are chosen randomly using a random generator

# Q 94
# Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
def perfect_parantheses(group: str):
    result = []
    temp = ''
    left_parantheses = 0
    right_parantheses = 0

    for string in group:
        if string == ' ':
            continue
        elif string == '(':
            left_parantheses += 1
            temp += string
        elif string == ')':
            right_parantheses += 1
            temp += string
            if left_parantheses == right_parantheses:
                result.append(temp)
                temp = ''
                left_parantheses = 0
                right_parantheses = 0
    return result

print(perfect_parantheses('( ()) ((()()())) (()) ()'))
print(perfect_parantheses('() (( ( )() ( )) ) ( ())'))

# Q 43
# Write a Python program to find all words in a given string with n consonants.