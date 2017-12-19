#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import os

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

	
	
#s1 = 72
#s2 = 85
#r = (s2 - s1)/s1 *100
#print('%.2f%%'%r) 
#print('{0:.2f}%'.format(r))


classmates = ['Mi','Xi','Do']
classmates.pop(1)
classmates[0] = 'So'
print(classmates)




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




sum = 0
for x in range(101):
	sum = sum + x
print(sum)



L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print(x)



n = 0
while n <= 100:
    n = n + 1
    if n > 10:
	    break
    if n % 2 == 0:
        continue
    print(n)



d = {'mm':90, 'nn':80, 'cc': 70}
d['mm'] = 80
d['mm'] = 77
#print(d['mmm'])
#print('mm' in d)
#print(d.get('mmm'), '无')	
d.pop('cc')
print(d)



s = set([1,5,32,3,4,2,1,22])
s.remove(1)
print(s)



s1 = set([1,2,3])
s2 = set([4,3,2])
#print(s1 & s2)
print(s1 | s2)



print(abs(100))
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))


#print(math.sqrt(2))


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




def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
        print('s=',s)
    return s

power(6)
power(5,4)



def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
#print(calc(1,2,3))
nums = [1,2,3]
print(calc(*nums))



def person(name, age, **kw):
  if 'city' in kw:
    print('city')
  if 'job' in kw:
    print('job')
  print('name:', name, 'age:', age, 'other', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)



def person(name, age, *, city='Beijing', job='Engineer'):
  print(name, age, city, job)

#person('Jack', 24, 'Beijing', 'Engineer')   false
person('Jack', 24, city = 'Shandong', job = 'Programmer')
#person('Jack', 24)


def product(*args):
    m = 1
    for n in args:
        m = n * m
    return m


if product(5) != 5:
    print('1测试失败!')
elif product(5, 6) != 30:
    print('2测试失败!')
elif product(5, 6, 7) != 210:
    print('3测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('4测试失败!')
else:
    try:
        product()
        print('5测试成功!')
    except TypeError:
        print('测试失败!')	




def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    print('num=',num,'product=',product)
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
fact(5)



def print_hanoi(n,A,B,C):
 if(n == 1):
   print(A,'-->',C)
 else:
   print_hanoi(n-1,A,C,B)
   print_hanoi(1,A,B,C)
   print_hanoi(n-1,B,A,C)

print_hanoi(3, 'A', 'B', 'C')



L = list(range(1,101))
#print(L[::2])
print(L[:10:2])
print(L[-10::2])
print(L[10:20:2])




def trim(s):
    while(s[0:1] == ' '):
        s = s[1:]
    while(s[-1:0] == ' '):
        s = s[0:-1]
    return s

print(trim(' 321 '))



L = [x*x for x in range(1,11)]
L1 = [x*x for x in range(1,11) if x%2 == 0]
L3 = [m+n for m in 'ABC' for n in 'MNB']
print(L3)


L = [d for d in os.listdir('.')]
print(L)


d = {'x':'A', 'Y':'B', 'Z':'C'}
for k, v in d.items():
    print(k, '=', v)
L = [k + '=' + v for k,v in d.items()]
print(L)


L1 = ['Hello', 'World', 18, 'Apple', None]
def ff(L1):
  L2 = []
  for x in L1:
    if isinstance(x,str):
      x = x.lower()
      L2.append(x)
  return L2
print(ff(L1))
print([s.lower() for s in L1 if isinstance(s,str)])  


g = (x*x for x in range(1,10))
print(g)
for x in g:
  print(x)
'''

'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'end' 

fib(6)	


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
	
g = fib(6)
while True:
        try:
            x = next(g)
            print('g:', x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break
	
	
for x in fib(6):
	print(x)	
'''

def triangles():
    L=[1]
    while True:
        yield L
        L=[L[i]+L[i+1] for i in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)



















