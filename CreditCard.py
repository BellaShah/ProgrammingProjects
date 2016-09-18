#  File: CreditCard.py

#  Description: This program checks the validity of credit card numbers and also the type of credit card. 

#  Student Name: Bella H Shah

#  Date Created: 10/22/2015

#  Date Last Modified: 10/25/2015

#This function checks if a 16 digit credit card number is valid
def sum_digits (n):
  sum_d = 0
  while (n > 0):
    sum_d = sum_d + n % 10
    n = n // 10
  return sum_d

#This function checks if a 16 digit credit card number is valid
def is_valid (cc_num):
  if len(str(cc_num)) !=15 and len(str(cc_num)) != 16:
    return 0
  b=str(cc_num)
  cnum=[]
  for digit in b:
    cnum.append(int(digit))
  even=cnum[::2] #a method of list splicing
  odd=cnum[1::2]
  even2=[2*i for i in even]
  sumdig_even=[sum_digits(i) for i in even2]
  all_num=sumdig_even+odd
  sum_all=sum(all_num)
  if sum_all%10==0:
    return cc_num
  else:
    return 2

#This function checks if a 15 digit credit card number is valid
def is_valid_15 (cc_num):
  if len(str(cc_num)) !=15 and len(str(cc_num)) != 16:
    return 0
  b=str(cc_num)
  cnum=[]
  for digit in b:
    cnum.append(int(digit))
  even=cnum[1::2] #a method of list splicing
  odd=cnum[::2]
  even2=[2*i for i in even]
  sumdig_even=[sum_digits(i) for i in even2]
  all_num=sumdig_even+odd
  sum_all=sum(all_num)
  if sum_all%10==0:
    return cc_num
  else:
    return 2
    
# This function returns the type of credit card
def cc_type(cc_num):
  if str(cc_num)[0] == '4':
    return "Visa"
  elif str(cc_num)[0:2] == '34' or str(cc_num)[0:2] == '37':
    return "American Express"
  elif str(cc_num)[0:2] == '65' or str(cc_num)[0:3] == '644' or str(cc_num)[0:4] == '6011':
    return "Discover"
  elif str(cc_num)[0:2] == '50' or str(cc_num)[0:2] == '51' or str(cc_num)[0:2] == '52' or str(cc_num)[0:2] == '53' or str(cc_num)[0:2] == '54' or str(cc_num)[0:2] == '55':
    return "Mastercard"
  else:
    return ""

#Prompts user to enter a credit card number and prints output based on number of digit, type and validity
def main():
  cc_num = int(input("Enter 15 or 16-digit credit card number:"))
  if is_valid(cc_num) == 0 or is_valid_15(cc_num) == 0:
    print("Not a 15 or 16-digit number")

  elif is_valid(cc_num) == 2 and is_valid_15(cc_num) == 2:
    print("Invalid credit card number")

  elif is_valid(cc_num) == cc_num or is_valid_15(cc_num)== cc_num:
    print("Valid", cc_type(cc_num), "credit card number")

main()