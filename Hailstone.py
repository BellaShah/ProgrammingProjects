#  File: Hailstone.py

#  Description: This program returns the longest cycle of the Hailstone sequence for a range of numbers

#  Student Name: Bella Shah

#  Date Created: September 19, 2015

#  Date Last Modified: September 20, 2015
def main():
	
  #Define variables
  max_length=0 #maximum cycle length
  num_max=0 #number having the maximum cycle
    
  #Prompts user to enter starting and ending number of range
  lo=int(input("Enter starting number of the range: ")) 
  hi=int(input("Enter ending number of the range: "))

  #Error checks the input
  while (lo<=0): 
    lo=int(input("Enter starting number of the range: "))
  while (hi<=0): 
    hi=int(input("Enter ending number of the range: "))
  while (lo>=hi):
    lo=int(input("Enter starting number of the range: "))
    hi=int(input("Enter ending number of the range: "))
        
  #Goes through each number in that range and calculates hailstone sequence  
  #Determines the cycle length 
  #Replaces max cycle length with current cycle length and num max with current number
  for counter in range((lo),(hi+1)): 
    cycle_length=0 
    num = counter 
    while (num>1): 
      if (num%2==1): 
        num=(3*num)+1
        cycle_length=cycle_length+1
      elif (num%2==0): 
        num=num//2
        cycle_length=cycle_length+1
    if (cycle_length>=max_length):  
      max_length=cycle_length 
      num_max=counter  

  #Prints result
  print ("The number "+str(num_max)+" has the longest cycle length of "+str(max_length)+".")

main()