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
def find_consonant_in_string(sentence, n):
    vowel = 'aeiou'
    result = []
    for word in sentence.split(' '):
        if sum(c not in vowel for c in word.lower()) == n:
            result.append(word)

    print("Number of consonants: ", n)
    print("Words in the string with", n, "consonants: ")
    print(*result, sep = ", ")

find_consonant_in_string('this is our time', 3)
find_consonant_in_string('this is our time', 2)
find_consonant_in_string('this is our time', 1)

# Q 18
# An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each row.
# Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed on them, but they are useful as arrays in computing.
# Write a Python program to find the indices of all occurrences of target in the uneven matrix.
def find_indices_in_uneven_matrix(arr, target):
    result = []

    for row_index, element in enumerate(arr):
        for col_index, item in enumerate(element):
            if item == target:
               result.append([row_index,col_index])

    # alternative: return [[i, j] for i, row in enumerate(arr) for j, n in enumerate(row) if n == target]
    return result

print(find_indices_in_uneven_matrix([[1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]], 19))
print(find_indices_in_uneven_matrix([[1, 2, 3, 2], [], [7, 9, 2, 1, 4]], 2))

# Q 58
# Write a Python program to find the biggest even number between two numbers inclusive.
def find_biggest_even_number(m:int , n: int):
    biggest = max(m,n)
    # if the biggest number is an even number, then we found it already, return immediately
    if biggest % 2 == 0:
        return biggest
    else: #the biggest number isn't an even number
        # subtract the biggest number with the remainder to get the biggest even number
        biggest = biggest - (biggest % 2)
        return biggest

print(find_biggest_even_number(12,51))
print(find_biggest_even_number(1,79))
print(find_biggest_even_number(47,53))
print(find_biggest_even_number(100,200))

# Q 24
# Write a Python program to create a list whose ith element is the maximum of the first i elements from an input list.
def create_new_list(num):
    new_list = [max(num[:i]) for i in range(1, len(num) + 1)]
    return new_list

print(create_new_list([0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]))
print(create_new_list([6, 5, 4, 3, 2, 1]))
print(create_new_list([1, 19, 5, 15, 5, 25, 5]))

# Q 39
# Write a Python program to determine which triples sum to zero from a given list of lists.
def sum_triples(arr):
    result = [sum(element) == 0 for element in arr]
    return result

print(sum_triples([[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]))
print(sum_triples([[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]))

# Q 25
# Write a Python program to find the XOR of two given strings interpreted as binary numbers.
def calc_xor(strings):
    result = '0b' + str(bin(int(strings[0],2) ^ int(strings[1], 2)))
    return result

print(calc_xor(['0001','1011']))
print(calc_xor(['100011101100001', '100101100101110']))

# Q 74
# Write a Python program to find a string consisting of space-separated characters with given counts.
def make_string(string: dict):
    # {'f': 1, 'o': 2}
    result = ''
    for key, val in string.items():
        result += key * val

    print(*result, sep= ' ')

make_string({'f': 1, 'o': 2})
make_string({'a': 1, 'b': 1, 'c': 1})

# Q 14
# Write a Python program to find the length of a given list of non-empty strings.
def find_length(array):
    result = [len(item) for item in array]
    return result

print(find_length(['cat', 'car', 'fear', 'center']))
print(find_length(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']))

# Q 82
# Write a Python program to find the sublist of numbers from a given list of numbers with only odd digits in increasing order.
def find_sublist_with_odd_num(num_array):
    result = sorted(filter(lambda x: x % 2 != 0, num_array))
    return result

print(find_sublist_with_odd_num([1, 3, 79, 10, 4, 2, 39]))
print(find_sublist_with_odd_num([11, 31, 40, 68, 77, 93, 48, 1, 57]))
print(find_sublist_with_odd_num([9, -2, 3, 4, -2, 0, 2, -3, 8, -1]))

# Q 79
# Write a Python program to find the largest negative and smallest positive numbers (or 0 if none).
def find_largest_negative_smallest_positive(num_array):
    negative_numbers = sorted(filter(lambda x: x < 0, num_array))
    positive_numbers = sorted(filter(lambda x: x >= 0, num_array))

    return [max(negative_numbers) if negative_numbers else 0, min(positive_numbers) if positive_numbers else 0]

print(find_largest_negative_smallest_positive([-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]))
print(find_largest_negative_smallest_positive([-1, -2, -3, -4]))
print(find_largest_negative_smallest_positive([1, 2, 3, 4]))
print(find_largest_negative_smallest_positive([]))

# Q 8
# Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
def split_words_into_lists(words):
    import re

    result = re.split(r'([ ,]+)', words)
    # array [start:stop:step]
    splitted_list = [result[::2], result[1::2]]

    return splitted_list

print(split_words_into_lists('W3resource Python, Exercises.'))
print(split_words_into_lists('The dance, held in the school gym, ended at midnight.'))
print(split_words_into_lists('The colors in my studyroom are blue, green, and yellow.'))

# Q 17
# Write a Python program to create a string consisting of non-negative integers up to n inclusive.
def create_string(n):
    new_string = ''.join(str(i) + ' ' for i in range(int(n)+1))
    return new_string

print(create_string(4))
print(create_string(15))

# Q 95
# Write a Python program to find a palindrome of a given length containing a given string.