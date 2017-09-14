while (1):
	n=raw_input("Enter:")
	if (n is 'a' or n is 'e' or n is 'i' or n is 'o' or n is 'u'):
		print "It is vowels"
	elif(n=='q'):
		exit()
	else:
		print "not a vowels"