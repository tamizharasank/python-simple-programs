# Python program to convert decimal number into binary, octal and hexadecimal number system
import sys
import time
import os
# Change this line for a different result
dec = int(input("Enter a value:\t"))
print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")
