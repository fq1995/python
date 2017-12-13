#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# name = input("please enter your name: ")
# print(name)

# number1 = input("number1: ")
# number2 = input("number2: ")
# print(number1 ,"*", number2, "=" , int(number1) * int(number2))

a=int(input('age:'))

if 18<=a<=59:
    print('welcome')
elif 0 <= a <=6:
    print('dont touch father"s pc')
elif a>=60:
    print('poor single dog')
else:
    print(18-a,'years later come')
