#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import os
from collections import Iterable, Iterator
from functools import reduce
import time,functools
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


def triangles():
    L=[1]
    while True:
        yield L
#        print('前  ',L)
        L=[L[i]+L[i+1] for i in range(len(L)-1)]
#        print('后  ',L)
        L.insert(0,1)
        L.append(1)

L = triangles();
for x in range(10):
#    next(L)
    print(next(L))


it = iter([1,2,3,4,5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break;


def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))




def fn(x,y):
    return x*10 + y

#print(reduce(fn, [0.1,2,3]))

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(char2num, '21332')))	



digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return digits[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num,s))



DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(str):
    index = str.find(".")
    length = 1
    if index >= 0:
        length = len(str[index + 1:])
        length = math.pow(10, length)
    str = str.replace('.','');
    return reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], str)) / length

#print('str2float(\'123456\') =', str2float('123456'))		
#print('str2float(\'123.456\') =', str2float('123.456'))
s = input("请输入数字：")
print(str2float(s))
print(float(s) == str2float(s))
#if abs(str2float('123.456') - 123.456) < 0.00001:
#    print('测试成功!')
#else:
#    print('测试失败!')



#### filter
# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
def not_empty(s):
    return s and s.strip()

L = list(filter(not_empty, ['A', '', 'B', ' ', None, 'C']))
print(L)

#用filter求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
output = filter(is_palindrome, range(1,100))
print(list(output))


#### sorted
s = sorted([36, 5, -12, 9, -21], key=abs)
print(s)

s = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse=True)
print(s)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return str.lower(t[0])
def by_score(t):
    return t[-1]
L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score)
L4 = sorted(L, key=by_score, reverse=True)

print(L2)
print(L3)
print(L4)

#### 返回函数
def calc_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = calc_sum(1,3,4,6)
print(f())


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


#利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    n = [0]
    def counter():
        n[0] = n[0] + 1
        return n[0]
    return counter

#使用 nonlocal 修改外层变量
def createCounter():
    x = 0
    def inner():
        nonlocal x
        x = x + 1
        return x
    return inner
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())


#### 匿名函数
f = lambda x: x*x
print(f(4))

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)


#### 装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper()

@log
def now():
    print('2015-2-3')

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(): ' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('excute')
def now():
    print('2015-2-3')

now()


# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(fn):
    def wrapper(*args, **kw):
        beg = time.time()*1000
        result = fn(*args, **kw)
        end = time.time()*1000
        print('%s excuted in %s ms' % (fn.__name__,end - beg))
        return result
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

f = fast(11, 22)
print(f)

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

s = slow(11, 22, 33)
print(s)
'''

