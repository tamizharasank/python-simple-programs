# n=int(input("Enter number of rows: "))
n=5
for i in range (n,0,-1):
    print((n-i) * ' ' + i * '*')
for g in range (6,0,-1):
	print(g * ' ' + (6-g) * '*')

	for i in range (1,6):  
    for j in range (5,i-1,-1):  
        print "*",  
    print  

    for i in range(7):
    print (str(i) + " ")*i

    for i in range(1, 8 + 1):
    for j in range(i, 0, -1):
        print(j),
    print("")

    for i in range(1, 9):
    for i in range(-1+i, -1, -1):
        print(format(2**i, "4d")),
    print

    for i in range(1, 9):
    for i in range(0,i,1):
        print(format(2**i, "4d")),
    for i in range(-1+i, -1, -1):
        print(format(2**i, "4d")),   
    print

    for i in range(1, 9):
    n = 34-(5*(i-1))+1
    print(" ")*n,
    for i in range(0,i,1):
        print(format(2**i, "4d")),
    for i in range(-1+i, -1, -1):
        print(format(2**i, "4d")),   
    print

    for i in range(1, 6):
    for j in range(65, 65+i):
        a = chr(j)
        print a,
    print

    from string import ascii_uppercase
for i in range(1, 6):
    print(" ".join(ascii_uppercase[:i]))

    