#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

# https://www.liaoxuefeng.com/

# name = input("please enter your name: ")
# print(name)

# number1 = input("number1: ")
# number2 = input("number2: ")
# print(number1 ,"*", number2, "=" , int(number1) * int(number2))

'''
a=int(input('age:'))
if 18<=a<=59:
    print('welcome')
elif 0 <= a <=6:
    print('dont touch father"s pc')
elif a>=60:
    print('poor single dog')
else:
    print(18-a,'years later come')
'''
	
	
#s1 = 72
#s2 = 85
#r = (s2 - s1)/s1 *100
#print('%.2f%%'%r) 
#print('{0:.2f}%'.format(r))

'''
classmates = ['Mi','Xi','Do']
classmates.pop(1)
classmates[0] = 'So'
print(classmates)
'''


'''
height = float(input('身高（米）'))
weight = float(input('体重（Kg）'))
bmi = weight/height/height
print ('%.1f' %bmi)
if bmi<18.5:
    print('过轻')
elif bmi<25:
    print('正常')
elif bmi<28:
    print('过重')
elif bmi<32:
    print('肥胖')
else:
    print('严重肥胖')

'''

'''
sum = 0
for x in range(101):
	sum = sum + x
print(sum)
'''

'''
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print(x)
'''

'''
n = 0
while n <= 100:
    n = n + 1
    if n > 10:
	    break
    if n % 2 == 0:
        continue
    print(n)
'''

'''
d = {'mm':90, 'nn':80, 'cc': 70}
d['mm'] = 80
d['mm'] = 77
#print(d['mmm'])
#print('mm' in d)
#print(d.get('mmm'), '无')	
d.pop('cc')
print(d)
'''

'''
s = set([1,5,32,3,4,2,1,22])
s.remove(1)
print(s)
'''

'''
s1 = set([1,2,3])
s2 = set([4,3,2])
#print(s1 & s2)
print(s1 | s2)
'''

'''
print(abs(100))

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
'''

#print(math.sqrt(2))

'''
def quadratic(a,b,c):
    for n in (a,b,c):
        if not isinstance(n, (int,float)):
	        raise TypeError('请输入数字')
    if a == 0 and b**2-4*a*c != 0:
        x = -c/b
        return x
    elif a != 0 and b**2-4*a*c > 0:
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x1,x2
    elif a != 0 and b**2-4*a*c == 0:
	    x = -b/(2*a)
	    return x
    else:
        return '无解'

print('quadratic(2,3,1) =', quadratic(2,3,1))
print('quadratic(1,3,-4) =', quadratic(1,3,-4))

'''

'''
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
        print('s=',s)
    return s

power(6)
power(5,4)
'''

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

#print(calc(1,2,3))

nums = [1,2,3]
print(calc(*nums))

