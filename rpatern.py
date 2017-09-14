n=5
t=2
for i in range(1,n):
	if i==1 or i==3:
		print "*"*(n)
	elif i==2:
		print '*',' '*(n-t)+'*'
for j in range(1,(i)):
	print "*",' '*(j)+'*'