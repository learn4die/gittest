#!/usr/bin/env python3


def enroll(name,gender,age=6,city='BeiJing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)
name=input('input your name:')
gender=input('input your gender:')
age=input('input your age:')
city=input('input your city:')
if age=='':
	age=6
if city=='':
	city='BeiJing'
enroll(name,gender,age,city)
'''
import math

def quadratic(a,b,c):
#	if not isinstance(a,b,c,(int,float)):
#		raise TypeError('bad operand type')
	delta=b*b-4*a*c	
	if delta<0:
		raise TypeError('there\'s no answer')
	return (-b+math.sqrt(delta))/(2*a),(-b-math.sqrt(delta))/(2*a)
a=eval(input('a:'))
b=eval(input('b:'))
c=eval(input('c:'))
x,y=quadratic(a,b,c)
rint('answer is:x1=%.2f,x2=%.2f'%(x,y))
'''





'''
names=['Michael','Bob','Tracy']
for name in names:
	print(name)

age=eval(input('input your age:'))
print('your age is',age)

if age>=18:
	print('adult')
else:
	print('teenager')
'''
