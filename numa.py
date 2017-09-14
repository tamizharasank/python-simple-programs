import os 
import time
a = 1
v = 0
print('enter number to add to the sum..')
print('enter 0 to quit.')
while a != 0:
	print('current sum',v)
	a = float(input('number:'))
	a = float(a)
	v += a
print('Total sum',v)	