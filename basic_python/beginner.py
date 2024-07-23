#!/usr/bin/python3

# Exercises based on https://www.w3resource.com/python-exercises/python-basic-exercises.php

#----- Q 1 ----------
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

#----- Q 2 ----------
import sys

print(sys.version)

#----- Q 3 ----------
import datetime

print(datetime.datetime.now)

#----- Q 4 ----------
# circle area = pi * r ^ 2
import math
r = float(input("Input the radius of the circle : "))
area = math.pi * math.pow(r,2)
print("Area of circle with radius: " + str(r) + " is " + str(area))

#----- Q 5 ----------
first_name = input("Input your first name: ")
last_name = input("Input your last name: ")

print(last_name + " " + first_name)

#----- Q 6 ----------
seq = input("Enter a sequence of numbers, seperate them by comma: ")

seq_list = seq.split(",")
seq_tuple = tuple(seq_list)

print("List : ", seq_list)
print("Seq : ", seq_tuple)

#----- Q 7 ----------
filename = input("Enter a filename: ")

file_extension = filename.split(".")
print("The extension of the file is :", repr(file_extension[-1])) #repr returns a printable representation of an object

#----- Q 8 ----------
color_list = ["Red","Green","White","Black"]

print("The first color is :", repr(color_list[0]))
print("The last color is :", repr(color_list[-1]))

#----- Q 9 ----------
exam_st_date = (11, 12, 2014)

print("The examination will start from : %i / %i / %i" % exam_st_date )

#----- Q 10 ----------
n = int(input("Input an integer: "))
print("Sample value of n is ", n)

n1 = n
n2 = int("%s%s" % (n,n))
n3 = int("%s%s%s" % (n,n,n))

result = n1 + n2 + n3

print("Result :", result)

#----- Q 11 ----------
#Print the docstring (documentation) of the 'abs' function
print(abs.__doc__)

#----- Q 12 ----------
import calendar

year = int(input("Input the year : "))
month = int(input("Input the month :"))

print(calendar.month(year, month))

#----- Q 13 ----------
# """ is a heredoc (string format is preserved)
print(
"""
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
""")

#----- Q 14 ----------
import datetime

date1 = datetime.date(2014,7,2)
date2 = datetime.date(2014,7,11)

diff_date = abs(date1 - date2)

print("The number of days between %s and %s is %s days" % (date1,date2,diff_date.days))

#----- Q 15 ----------
#volume of sphere with radius 6
# V = 4/3 * pi * r ^ 3
import math

radius = 6
volume = 4/3 * math.pi * math.pow(radius,3)
print("The volume of spehere with radius %i is %f" % (radius, volume))

#----- Q 16 ----------
#difference between number and 17. if num > 17, return 2 * abs(diff)

num = int(input("Input a number : "))
if (num > 17):
    diff = 2 * abs(num - 17)
else:
    diff = abs(num - 17)

print(diff)

#----- Q 17 ----------
# Write a Python program to test whether a number is within 100 of 1000 or 2000.
def test_val(n):
    if (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100):
        return True
    else:
        return False

print(test_val(1200))
print(test_val(1990))

#----- Q 18 ----------
def sum_of_three_num(a: int, b: int, c: int):
    if a == b and b == c:
        return 3 * (a + b + c)
    else:
        return a + b + c

print(sum_of_three_num(1,2,3))
print(sum_of_three_num(3,3,3))

#------ Q 19 -----------
def add_ls(text):
    if text.startswith('Is'):
        return text
    else:
        return "Is" + text

print(add_ls("abls"))
print(add_ls("Ispop"))

#------ Q 20 -----------
def str_copy(text, n):
    if n == 1:
        return text
    else:
        tmp = ""
        for i in range(n):
            tmp += text
        return tmp

print(str_copy("hello",2))

#------ Q 21 -----------
def even_or_odd():
    n = int(input('Please input a number: '))
    if n % 2 == 0:
        print("the number is an even number")
    else:
        print("the number is an odd number")

#------ Q 22 -----------
def total_four_in_list(lst):
    total = 0
    for item in lst:
        if item == 4:
            total += 1
    return total

print(total_four_in_list([3,4,5,6,4,5,4,21,20,45]))

#------ Q 23 -----------
def str_char_copy(text: str, n):
    if len(text) < 2:
        return str_copy(text, n)
    else:
        tmp = text[:2]
        return str_copy(tmp,n)

print(str_char_copy('popopoplk',3))
print(str_char_copy('k',30))

#------ Q 24 -----------
def vowel_or_not(letter):
    return letter in 'AEIOUaeiou'

print(vowel_or_not('b'))
print(vowel_or_not('e'))

#------ Q 25 -----------
def contain_value(value):
    test_data = [1, 5, 8, 3]
    for val in test_data:
        if value == val:
            return True
    return False

print(contain_value(3))
print(contain_value(-1))

#------ Q 26 -----------
def create_histogram(lst):
    for num in lst:
        tmp = ''
        for i in range(num):
            tmp += '*'
        print(tmp)

create_histogram([2,3,4])

#------ Q 27 -----------
def concat_elements_in_list(lst):
    result = ''
    for item in lst:
        result += item
    return result

print(concat_elements_in_list(['hello', 'world', 'its', 'me']))

#------ Q 28 -----------
def print_even(lst):
    for num in lst:
        if num == 237:
            print(num)
            break
        elif num % 2 == 0: #the number is even
            print(num)

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
print_even(numbers)

#------ Q 29 ----------
def color_not_present(color_list_1, color_list_2):
    result = set()
    for color in color_list_1:
        if color not in color_list_2:
            result.add(color)
    return result

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_not_present(color_list_1, color_list_2))

#------ Q 30 ----------
def compute_triangle_area(base, height):
    area = 1/2 * float(base) * float(height)
    return area

print(compute_triangle_area(24,5.6))

#------ Q 31 ----------
import math
def greatest_common_divisor(n1, n2):
    return math.gcd(n1, n2)

print(greatest_common_divisor(34,7))

#------ Q 32 ----------
def least_common_multiple(n1, n2):
    return math.lcm(n1, n2)

print(least_common_multiple(4,6))

#------ Q 33 ----------
def sum_of_3(a, b, c):
    if a == b or b == c or a == c:
        return 0
    return a + b + c

print(sum_of_3(1,2,3))
print(sum_of_3(9,10,9))

#------ Q 34 ----------
def sum_of_2(a, b):
    total = a + b
    if total in range(15,20): #inclusive on 15, exclusive on 20
        return 20
    return total

print(sum_of_2(23,10))
print(sum_of_2(9,7))

#------ Q 35 ----------
def test_numbers(a ,b):
    if a == b or a + b == 5 or abs(a-b) == 5:
        return True
    else:
        return False
#------ Q 36 ----------
print(test_numbers(12,7))
print(test_numbers(0,0))

def add_if_int(obj1, obj2):
    if type(obj1) == int and type(obj2) == int: #or can use isinstance(obj1, int)
        return obj1 + obj2
    else:
        return 'Inputs must be integers'

print(add_if_int(9,10))
print(add_if_int('9','10'))

#------ Q 37 ----------
def display_details():
    name = 'Ali'
    age = '33'
    address = 'Tokyo'

    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

display_details()

#------ Q 38 ----------
def quadratic(x, y):
    result = x * x + 2 * x * y + y * y
    print("({} + {}) ^ 2 = {}".format(x, y, result))

quadratic(4,3)

#------ Q 39 ----------
# A = P(1 + r/n)^nt, A: final amt, P: initial principal bal, r: annual interest rate, n: no of times interest is compounded per year, t: time (in years)
amt = 10000
intrest = 3.5
years = 7

future_val = amt * ((1 + (intrest * 0.01)) ** years )
print(round(future_val, 2))

#------ Q 40 ----------
def distance_btwn_points(p1, p2):
    distance = math.sqrt( ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    print(distance)

distance_btwn_points([4,0], [6,6])

#------ Q 41 ----------
#check if file exists
import os.path

print(os.path.isfile('main.txt'))

#------ Q 42 ----------
#check if python shell is executing in 32bit or 64bit mode on OS
import platform
import struct

architecture = platform.architecture()[0] #since the first item in the tuple contain information about the bit architecture
print(architecture)

#determine the size (in bytes) of the C int type for curr platform
print(struct.calcsize("P") * 8)

#------ Q 43 ----------
# get OS name, platform and release info
print("Name of operating system: ", os.name)
print("Name of the OS system: ", platform.system())
print("Version of operating system: ", platform.release())

#------ Q 44 ----------
# locate python site packages
# important to understand where Python packages are installed on particular system; to manage dependencies in Python proj
import site

print(site.getsitepackages())

#------ Q 45 ----------
# calls an external command
import os

print(os.system('dir'))

#------ Q 46 ----------
# retrieve path and name of file curr executed
print("Current File Name: ", os.path.realpath(__file__))

#------ Q 47 ----------
# find no of CPUs used
import multiprocessing

print(multiprocessing.cpu_count())

#------ Q 48 ----------
# parse a str to float / int
n = "2398.432"

str_2_float = float(n)
str_2_int = int(float(n))

print(str_2_float)
print(str_2_int)

#------ Q 49 ----------
# list all files in a directory
from pathlib import Path

for root, dirs, files in Path("/Users/Nadhira Shah/OneDrive - Liquid-Markets-Holdings Inc/Desktop/1 july").walk():
    for name in files:
        print(name)

#------ Q 50 ----------
# print without newline or space
for i in range(10):
    print('*', end="")

#------ Q 51 ----------
# determine the profiling of Python programs
import cProfile
import re
cProfile.run('re.compile("foo|bar")')

#------ Q 52 ----------
# print to STDERR
import sys
print('hello world!', file=sys.stderr)

#------ Q 53 ----------
# access environment variables
print(os.environ)

#------ Q 54 ----------
# get current username
print(os.getlogin())

#------ Q 55 ----------
# find local IP address using Python's stdlib
import socket

# get local hostname
local_hostname = socket.gethostname()
print(local_hostname)

# get list of IP address associated with the hostname
ip_address = socket.gethostbyname_ex(local_hostname)[2]
print(ip_address)

# filter out loopback addresses (IPs starting with 127.)
filtered_ips = [ip for ip in ip_address if not ip.startswith("127.")]

# extract the first ip address (if available) from the filtered list
first_ip = filtered_ips[0]

print(first_ip)

#------ Q 56 ----------
# get height and width of console window
import os

terminal_size = os.get_terminal_size()
width = terminal_size[0]
height = terminal_size[1]
print("width of console window is: ", width)
print("height of console window is: ", height)

#------ Q 57 ----------
# execution event monitoring
import timeit

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

#------ Q 58 ----------
# sum the first n positive integers
n = int(input("Input a number: "))

# calculate the sum of the first 'n' positive integers
numbers = [i for i in range(n+1)]
print(sum(numbers))

#------ Q 59 ----------
# convert height (in ft and inches) to cm
# cm = ft x 30.48 + inch x 2.54
def convert_2_cm():
    ft = int(input("Feet: "))
    inch = int(input("Inches: "))
    result = round(int(ft * 30.48 + inch * 2.54), 1)
    return result

print(convert_2_cm())

#------ Q 60 ----------
# calculate hypotenuse of right angled triangle
import math

def calc_hypotenuse():
    a = int(input("Input the height of the right angled triangle: "))
    b = int(input("Input the width of the right angled triangle: "))

    c = int(math.sqrt(math.pow(a,2) + math.pow(b,2)))
    return c

print(calc_hypotenuse())

#------ Q 61 ----------
# convert distance (in ft) to inches, yard, miles
# 1 foot = 12 inches
# 1 yard = 3 feet
# 1 yard = 36 inches
# 1 mile = 1760 yards
def convert_distance():
    feet = int(input("Feet: "))
    inches = feet * 12
    yard = feet/3
    mile = yard/1760

    print("{} feet is equal to {} inches, {:0.2f} yard and {:0.2f} mile".format(feet, inches, yard, mile))

convert_distance()

#------ Q 62 ----------
# convert all unit of time into seconds
# 1 day = 24 hours
# 1 hr = 60 min
# 1 min = 60 sec
def convert_time():
    #prompt user to input number of days, hours, min, sec and convert it all to sec
    days = int(input("Input days: ")) * 24 * 3600
    hours = int(input("Input hours: ")) * 3600
    minutes = int(input("Input minutes: ")) * 60
    seconds = int(input("Input seconds: "))

    time = days + hours + minutes + seconds

    print("The amount of seconds:", time)

convert_time()

#------ Q 63 ----------
# get an absolute file path
# os.path.abspath(path)
def absolute_file_path(fname_path):
    import os
    
    return os.path.abspath(fname_path)

print('Absolute file path: ', absolute_file_path('beginner.py'))

#------ Q 64 ----------
# retrieve date and time file creation and modification
def get_file_info(fname_path):
    import os, time

    print('Last modified: ', time.ctime(os.path.getmtime(fname_path)))
    print('Created: ', time.ctime(os.path.getctime(fname_path)))

get_file_info('beginner.py')

#------ Q 65 ----------
def convert_seconds():
    time = float(input("Input time in seconds: "))
    days = time / (24 * 3600)
    time = time % (24 * 3600) # update time with the remaining secs
    hours = time / 3600
    time = time % 3600 # update time with the remaining secs
    minutes = time / 60
    time = time % 60 # update time with the remaining secs
    seconds = time

    print("day:hour:minutes:seconds -> %d:%d:%d:%d" % (days, hours, minutes, seconds))

convert_seconds()

#------ Q 66 ----------
def calc_bmi():
    height = float(input("Height in meter: "))
    weight= float(input("Weight in kg: "))

    bmi = round(weight / (height ** 2), 1)
    print("BMI for height: {} and weight: {} is {}".format(height, weight, bmi))

calc_bmi()

#------ Q 67 ----------
# convert pressure in kilopascals to pound/sq inch, a milimeter of mercury (mmHg) and atmosphere pressure
# 1 Psi = 6.89476 Kpa
# 1 kPa = 7.50062 mmHg
# 1 kPa = tel:00098692327 atm
def convert_pressure():
    kpa = float(input("Pressure in kilopascals: "))
    psi = kpa / 6.89476
    mmhg = kpa * 7.50062
    atm = kpa * tel:00098692327
    print("Pressure in pounds per square inch: %.2f psi" % psi)
    print("Pressure in milimeter of mercury: %.2f mmHg" % mmhg)
    print("Atmosphere pressure: %.2f atm" % atm)

convert_pressure()

#------ Q 68 ----------
# calculate sum of digits of number
def sum_of_digits():
    num = str(input("Input a digit: "))
    result = 0

    for i in range(len(num)):
        result += int(num[i])

    print("The sum of digits {} is {}".format(num, result))

sum_of_digits()

#------ Q 69 ----------
# sort 3 int without using conditional statements and loops
def sort_int():
    a = int(input("Input 1st integer: "))
    b = int(input("Input 2nd integer: "))
    c = int(input("Input 3rd integer: "))

    max_val = max(a, b, c)
    min_val = min(a, b, c)
    mid_val = (a+b+c) - max_val - min_val

    print(f"The 3 integers sorted: {min_val} {mid_val} {max_val}")

sort_int()

#------ Q 70 ----------
def sort_files_by_date():
    import glob
    import os

    files = glob.glob("*.txt")
    sorted_files = sorted(files, key=os.path.getmtime)

    # Print the sorted list of file names, one per line.
    print("\n".join(map(str, sorted_files)))

sort_files_by_date()

#------ Q 71 ----------
# get directory listing, sorted by creation date
def list_dir():
    import os

    directory = os.listdir(path='.')
    sorted_dir = sorted(directory, key=os.path.getctime)

    print(sorted_dir)

list_dir()

#------ Q 72 ----------
# get details of math module
import math
help(math)

#------ Q 73 ----------
def calc_midpoint_of_line():
    p1 = [4,0]
    p2 = [6,6]

    midpoint_x = (p1[0] + p2[0]) / 2
    midpoint_y = (p1[1] + p2[1]) / 2

    print("Midpoint of the line is {} {}".format(midpoint_x, midpoint_y))

calc_midpoint_of_line()