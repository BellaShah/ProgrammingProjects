#  File: FibonacciBase.py

#  Description: This program shows a binary representation of the numbers that are used in the Fibonacci series.

#  Student Name: Bella H Shah

#  Date Created: 11/05/2015

#  Date Last Modified: 11/05/2015
def convert_fib_base (num):
	#Computes the fibonacci series and appends to a list
	if num == 0 : 
		return 0
	fib = [2,1]
	while fib[0] < num: 
		fib[0:0] = [sum(fib[:2])]
	bin = []
	
	#Finds the binary representation of the input number 
	for i in fib:
		if i <= num:
			bin = bin + [1]
			num = num - i
		else:
			bin += [0]
	
	#Deletes the leading zero, if any and concatinates the binary number as a string and returns the binary number
	bin_num = ""
	if bin[0] == 0:
		bin.remove(0)
	for b in bin: 
		bin_num += str(b)

	return bin_num  

def main():
	#Prompts user for decimal number and calls function to convert decimal number to binary.
	DECIMAL_NUM = int(input("Enter a number: "))
	BINARY_NUM_IN_FIB_BASE = convert_fib_base(DECIMAL_NUM)
	print (DECIMAL_NUM,"=", BINARY_NUM_IN_FIB_BASE,"(fib)")	
main()