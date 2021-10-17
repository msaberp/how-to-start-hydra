"""
Argument management using argparse library

link of the documentation:
https://docs.python.org/3.8/library/argparse.html

input:
>>> python lessons/lesson_2.py --number1 3 --number2 7 --action max

output:
>>> number 1: 3
>>> number 2: 7
>>> action: max
>>> results: 7

"""

import argparse


parser = argparse.ArgumentParser(description='Manage the given arguments.')
parser.add_argument('-n', '--number1', type=int, default=0, help='the first input number')
parser.add_argument('-m', '--number2', type=int, default=0, help='the first input number')
parser.add_argument('-a', '--action', type=str, default='sum', help='the action you want to apply on the two given numbers. [sum, max, min]')

args = parser.parse_args()

num1 = args.number1
num2 = args.number2
action = args.action

print("\n")
print(f"number 1: {num1}")
print(f"number 2: {num2}")
print(f"action: {action}")
print("\n")

if action == 'sum':
    print(f"result: {num1 + num2}")
elif action == 'max':
    print(f"result: {max(num1, num2)}")
elif action == 'min':
    print(f"results{min(num1, num2)}")
else:
    raise Exception(f"the given action [{action}] is not in the list of available actions: [sum, max, min]")