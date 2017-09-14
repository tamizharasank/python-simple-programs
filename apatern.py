n=6
t=3
for i in range(1,n):
	if i==1 or i==3:
		print "*"*(n)
	elif i==2:
		print "*"," "*(n-t)+"*"
	else:
		print "*"," "*(n-t)+"*"