# n=int(input("Enter the number of rows:"));
n=5
for i in range(1,n):  
	print format(' '*(n-(i+1))+str(i)*i+str(i)*(i-1))
	