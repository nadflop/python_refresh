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
def find_palindrome(string, length):
    # check if the given string is a palindrome
    def check(curr_string, reverse_string):
        return curr_string == reverse_string

    # convert the string to lowercase, and strip all whitespace
    temp = str(string).lower().strip(' ')

    # check if the current string length matches the given length
    if len(temp) == length:
        reverse = temp[::-1]
        if check(temp, reverse):
            return reverse

    # the string isn't a palindrome by default, so we will rebuild it
    s_index = 0
    # calculate half length of palindrome
    length_half = (length - (length % 2)) // 2
    ans = ''

    # build the first half of palindrome
    while len(ans) < length_half:
        ans += string[s_index % len(string)]
        s_index += 1

    # if length is odd
    if length % 2 != 0:
        ans += "a"

    # complete palindrome by adding the reversed first half
    reverse = ans + ans[::-1]
    return reverse

print(find_palindrome('madam', 7))
print(find_palindrome('madam', 6))
print(find_palindrome('madam', 5))
print(find_palindrome('madam', 3))
print(find_palindrome('madam', 2))
print(find_palindrome('madam', 1))

# Q 68
# Write a Python program to find all 5's in integers less than n that are divisible by 9 or 15.
# the number must be in range(n), output must consists of the number that is divisible by 9 or 15, and the index of int '5' in the number
# eg: 15 -> index 5 is 1, 105 -> index 5 is 2
def find_five_in_integer(number: int):
    result = [[i, j] for i in range(number) for j in range(len(str(i))) if str(i)[j] == '5' and (i % 9 == 0 or i % 15 == 0)]

    return result

print(find_five_in_integer(50))
print(find_five_in_integer(65))
print(find_five_in_integer(75))
print(find_five_in_integer(85))
print(find_five_in_integer(150))

# Q 62
# Write a Python program to find the dictionary key whose case is different from all other keys.
def find_odd_dict_key(dictionary: dict):
    keys = [key for key in dictionary.keys()]

    for k in dictionary.keys():
        if all(str(k).islower() != str(item).islower() for item in keys if k != item):
            return k

print(find_odd_dict_key({'red': '', 'GREEN': '', 'blue': 'orange'}))
print(find_odd_dict_key({"RED": "", "GREEN": "", "orange": "#125GD"}))

# Q 86
# Write a Python program to find the vowels from each of the original texts (y counts as a vowel at the end of the word) from a given list of strings.
def find_vowels(texts):
    vowels = 'aeiou'
    result = ["".join(filter(lambda x: x.lower() in vowels, word)) + (word[-1] if word[-1].lower() == 'y' else '') for word in texts]

    return result

print(find_vowels(['w3resource', 'Python', 'Java', 'C++']))
print(find_vowels(['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']))

# Q 40
# Write a Python program to find strings that, when case is flipped, give a target where vowels are replaced by characters two later.
def flip_string(word):
    import string
    alphabet = string.ascii_letters
    new_string = [w for w in word.swapcase()]

    for index, char in enumerate(new_string):
        if char in 'aeiouAEIOU':
            new_string[index] = alphabet[alphabet.index(char) + 2]

    result = "".join(w for w in new_string)
    return result

print(flip_string('Python'))
print(flip_string('aeiou'))
print(flip_string('Hello, world!'))
print(flip_string('AEIOU'))

# Q 21
# Write a Python program to check, for each string in a given list, whether the last character is an isolated letter or not. Return True otherwise False.
def check_if_lastchar_is_isolated(array):
    result = [string[-2] == ' ' for string in array]

    return result

print(check_if_lastchar_is_isolated(['cat', 'car', 'fear', 'center']))
print(check_if_lastchar_is_isolated(['ca t', 'car', 'fea r', 'cente r']))

# Q 1
# Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
def find_exact_occurences(array):
    return array.count(19) == 2 and array.count(5) >= 3

print(find_exact_occurences([19, 19, 15, 5, 3, 5, 5, 2]))
print(find_exact_occurences([19, 15, 15, 5, 3, 3, 5, 2]))
print(find_exact_occurences([19, 19, 5, 5, 5, 5, 5]))

# Q 90
# For each triple of eaten, need, and stock, write a Python program to get a pair of total appetite and remaining.
# input: eaten, need, stock
# output: total appetite = eaten + need, remaining stock after needs are fulfiled = stock - need
def count_total_appetite_and_remaining(nums):
    result = [[eaten + min(need, stock), max(0, stock - need)] for eaten, need, stock in nums]
    return result

print(count_total_appetite_and_remaining([[2, 5, 6], [3, 9, 22]]))
print(count_total_appetite_and_remaining([[2, 3, 18], [4, 9, 2], [2, 5, 7], [3, 8, 12], [4, 9, 106]]))
print(count_total_appetite_and_remaining([[1, 2, 3], [4, 5, 6]]))

# Q 83
# A string is happy if every three consecutive characters are distinct. Write a Python program to find two indices associated with a given string being unhappy.
def find_unhappy_indices(string):
    for index, char in enumerate(string.lower()):
        if index+1 < len(string) and char == string[index+1].lower():
            return [index, index+1]
        elif index+1 < len(string) and char == string[index+2].lower():
            return [index, index+2]
    return None

print(find_unhappy_indices('Python'))
print(find_unhappy_indices('Unhappy'))
print(find_unhappy_indices('Find'))
print(find_unhappy_indices('Street'))

# Q 48
# Write a Python program to find the indices of two entries that show that the list is not in increasing order. If there are no violations (they are increasing), return an empty list.
def find_violating_entries(array):
    result = [index for index, char in enumerate(array) if index+1 < len(array) and char > array[index+1]]
    if len(result) != 0:
        result.append(result[0]+1)

    return result

print(find_violating_entries([1, 2, 3, 0, 4, 5, 6]))
print(find_violating_entries([1, 2, 3, 4, 5, 6]))
print(find_violating_entries([1, 2, 3, 4, 6, 5, 7]))
print(find_violating_entries([-3, -2, -3, 0, 2, 3, 4]))

# Q 69
# Write a Python program to create a new string by taking a string, and word by word rearranging its characters in ASCII order.
def rearrange_string_in_ascii_order(sentence):
    return " ".join("".join(sorted(char)) for char in sentence.split(" "))

print(rearrange_string_in_ascii_order('Ascii character table'))
print(rearrange_string_in_ascii_order('maltos won'))

# Q 5
# Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.
def check_proper_substring(array):
    return array[-2] in array[-1]

print(check_proper_substring(['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
print(check_proper_substring(['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']))
print(check_proper_substring(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']))
print(check_proper_substring(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']))

# Q 50
# Write a Python program to find even-length words from a given list of words and sort them by length.
def find_and_sort_even_length_words(array):
    return sorted(filter(lambda x: len(x) % 2 == 0, array), key= len)

print(find_and_sort_even_length_words(['Red', 'Black', 'White', 'Green', 'Pink', 'Orange']))
print(find_and_sort_even_length_words(['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']))

# Q 77
# Write a Python program to convert GPAs to letter grades according to the following table:
# GPAs | Grades
# 4.0 | A+
# 3.7 | A
# 3.4 | A-
# 3.0 | B+
# 2.7 | B
# 2.4 | B-
# 2.0 | C+
# 1.7 | C
# 1.4 | C-
# below | F
def convert_gpa_to_letter_grades(gpas):
    result = []
    for gpa in gpas:
        if gpa >= 4.0:
            result.append('A+')
        elif gpa < 4.0 and gpa >= 3.7:
            result.append('A')
        elif gpa < 3.7 and gpa >= 3.4:
            result.append('A-')
        elif gpa < 3.4 and gpa >= 3.0:
            result.append('B+')
        elif gpa < 3.0 and gpa >= 2.7:
            result.append('B')
        elif gpa < 2.7 and gpa >= 2.4:
            result.append('B-')
        elif gpa < 2.4 and gpa >= 2.0:
            result.append('C+')
        elif gpa < 2.0 and gpa >= 1.7:
            result.append('C')
        elif gpa < 1.7 and gpa >= 1.4:
            result.append('C-')
        elif gpa < 1.4:
            result.append('F')

    return result

print(convert_gpa_to_letter_grades([4.0, 3.5, 3.8]))
print(convert_gpa_to_letter_grades([5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]))

# Q 33
# Write a Python program to find the positions of all uppercase vowels (not counting Y) in even indices of a given string.
def find_uppercase_vowel_with_even_indices(word):
    return [index for index, char in enumerate(word) if index % 2 == 0 and char in 'aeiouAEIOU']

print(find_uppercase_vowel_with_even_indices('w3rEsOUrcE'))
print(find_uppercase_vowel_with_even_indices('AEIOUYW'))

# Q 52
# Write a Python program to reverse the case of all strings. For those strings, which contain no letters, reverse the strings.
def reverse_case_of_all_strings(strings):
    return [word.swapcase() if word.isalpha() else word[::-1] for word in strings]

print(reverse_case_of_all_strings(['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']))
print(reverse_case_of_all_strings(['Green', 'Red', 'Orange', 'Yellow', '', 'White']))
print(reverse_case_of_all_strings(['Hello', '!@#', '!@#$', '123#@!']))

# Q 39
# Write a Python program to determine which triples sum to zero from a given list of lists.
def find_sum_of_zero(array):
    return [sum(num) == 0 for num in array]

print(find_sum_of_zero([[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]))
print(find_sum_of_zero([[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]))

# Q 100
# Write a Python program to find four positive even integers whose sum is a given integer.
def find_integers_for_given_sum(num):
    set_of_integers = [2,2,2,2]

    if num > 1000:
        set_of_integers[0] = 800

    while(sum(set_of_integers) != num):
        set_of_integers[0] += 2

    return set_of_integers

print(find_integers_for_given_sum(100))
print(find_integers_for_given_sum(1000))
print(find_integers_for_given_sum(10000))
print(find_integers_for_given_sum(1234567890))