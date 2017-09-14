import os
import sys
import time

# while True:
# 	pass
# 	print"%s\n"%time.ctime()
# 	time.sleep(1)
# 	print"%s"%time.ctime()

def add(n,n1):
	return n + n1

def sub(n,n1):
	return n - n1

def mul(n,n1):
	return n * n1

def div(n,n1):
	return n / n1

print "1.add\n2.subtract\n3.multiply\n4.divide\n"
c = input('Enter your choice(1/2/3/4):')
if c == 1:
	n = int(input('Enter 1st number:'))
	n1 = int(input('Enter 2nd number:'))
	print "addition of",n,"&",n1,"number is =>",add(n,n1)
elif c == 2:
	n = int(input('Enter 1st number:'))
	n1 = int(input('Enter 2nd number:'))
	print "sub of",n,"&",n1,"number is =>",sub(n,n1)
elif c == 3:
	n = int(input('Enter 1st number:'))
	n1 = int(input('Enter 2nd number:'))
	print "multiply of",n,"&",n1,"number is =>",mul(n,n1)
elif c == 4:
	n = int(input('Enter 1st number:'))
	n1 = int(input('Enter 2nd number:'))
	print "divide of",n,"&",n1,"number is =>",div(n,n1)
else:
	print "invalid input"