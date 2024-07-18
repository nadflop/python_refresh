#!/usr/bin/python3

# Exercises based on https://www.w3resource.com/python-exercises/python-basic-exercises.php

'''print("----Q1----\n")
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

print("\n----Q2----\n")
import sys

print(sys.version)

print("\n----Q3----\n")
import datetime

print(datetime.datetime.now)

print("\n----Q4----\n")
# circle area = pi * r ^ 2
import math
r = float(input("Input the radius of the circle : "))
area = math.pi * math.pow(r,2)
print("Area of circle with radius: " + str(r) + " is " + str(area))

print("\n----Q5----\n")
first_name = input("Input your first name: ")
last_name = input("Input your last name: ")

print(last_name + " " + first_name)

print("\n----Q6----\n")
seq = input("Enter a sequence of numbers, seperate them by comma: ")

seq_list = seq.split(",")
seq_tuple = tuple(seq_list)

print("List : ", seq_list)
print("Seq : ", seq_tuple)

print("\n----Q7----\n")
filename = input("Enter a filename: ")

file_extension = filename.split(".")
print("The extension of the file is :", repr(file_extension[-1])) #repr returns a printable representation of an object

print("\n----Q8----\n")
color_list = ["Red","Green","White","Black"]

print("The first color is :", repr(color_list[0]))
print("The last color is :", repr(color_list[-1]))

print("\n----Q9----\n")
exam_st_date = (11, 12, 2014)

print("The examination will start from : %i / %i / %i" % exam_st_date )

print("\n----Q10----\n")
n = int(input("Input an integer: "))
print("Sample value of n is ", n)

n1 = n
n2 = int("%s%s" % (n,n))
n3 = int("%s%s%s" % (n,n,n))

result = n1 + n2 + n3

print("Result :", result)

print("\n----Q11----\n")
#Print the docstring (documentation) of the 'abs' function
print(abs.__doc__)

print("\n----Q12----\n")
import calendar

year = int(input("Input the year : "))
month = int(input("Input the month :"))

print(calendar.month(year, month))

print("\n----Q13----\n")
# """ is a heredoc (string format is preserved)
print(
"""
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
""")

print("\n----Q14----\n")
import datetime

date1 = datetime.date(2014,7,2)
date2 = datetime.date(2014,7,11)

diff_date = abs(date1 - date2)

print("The number of days between %s and %s is %s days" % (date1,date2,diff_date.days))

print("\n----Q15----\n")
#volume of sphere with radius 6
# V = 4/3 * pi * r ^ 3
import math

radius = 6
volume = 4/3 * math.pi * math.pow(radius,3)
print("The volume of spehere with radius %i is %f" % (radius, volume))
'''
print("\n----Q16----\n")
#difference between number and 17. if num > 17, return 2 * abs(diff)

num = int(input("Input a number : "))
if (num > 17):
    diff = 2 * abs(num - 17)
else:
    diff = abs(num - 17)

print(diff)

print("\n----Q17----\n")
#