n=int(input("Enter the number:"))
t=int(input("Enter the range:"))
for i in range(1):
	for j in range(n):
		print '*',
	print
	for k in range(t):
		print ' '*(j-1),"*" 
		