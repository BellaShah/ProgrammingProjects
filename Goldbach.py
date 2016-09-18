#  File: Goldbach.py

#  Description: This program tests Goldbach's conjecture

#  Student Name: Bella Shah

#  Date Created: September 20, 2015

#  Date Last Modified: September 24, 2015

#Checks if number is prime
def is_prime (n):
  limit = int (n ** 0.5) + 1
  divisor = 2
  while (divisor < limit):
    if (n % divisor == 0):
      return False
    divisor = divisor + 1
  return True

def main():
#Prompts user to enter lower limit and upper limit
  lower=int(input("Enter the lower limit: ")) 
  upper=int(input("Enter the upper limit: "))

#Error checks the input
  while (lower<4 or lower%2!=0 or upper<4 or lower>=upper):
    lower=int(input("Enter the lower limit: "))
    upper=int(input("Enter the upper limit: "))

#Goes through each even number in range from lower to upper limit
#Finds which two prime numbers add up to the even number and prints result
  for num in range((lower),(upper+1),2): 
    even_num=num
    print (even_num, end ="")
    result = ""
    for a in range(2,even_num+1):
      if (is_prime(a)):
        b = even_num - a
        if (is_prime(b) and a<=b):
          result += " = " + str(a) + " + " + str(b)
    print (result)                
main()