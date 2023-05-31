#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

print(happy_new_year())

def square_integers(int_list):
    int_list = [num ** 2 for num in int_list]
    return int_list

def fizzbuzz():
    i = 1
    while i < 101:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
        i += 1
