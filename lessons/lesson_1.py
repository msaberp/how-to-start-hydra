"""
Argument managment using sys library

input:
>>> python lessons/lesson_1.py arg1 arg2 arg3

output:
>>> This is the name of the program: lessons/lesson_1.py
>>> This is the 1th argument: arg1
>>> This is the 2th argument: arg2
>>> This is the 3th argument: arg3

"""

import sys


for arg_idx, arg in enumerate(sys.argv):
    if arg_idx == 0:
        print(f"This is the name of the program: {arg}")
    else:
        print(f"This is the {arg_idx}th argument: {arg}")

