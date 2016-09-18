
#  File: EasterSunday.py

#  Description: This program computes the date  of Easter Sunday.

#  Student Name: Bella H Shah

#  Date Created: 09/06/2015

#  Date Last Modified: 09/09/2015

def main():
  #prompt the user to enter year
  y = int (input ("Enter year: "))

  #compute a
  a = y%19

  #compute b
  b = y//100

  #compute c
  c = y%100

  #compute d
  d = b//4

  #compute e
  e = b%4

  #compute g
  g = (8*b+13)//25

  #compute h
  h = (19*a+b-d-g+15)%30

  #compute j
  j = c//4

  #compute k
  k = c%4 

  #compute m 
  m = (a+11*h)//319

  #compute r
  r = (2*e+2*j-k-h+m+32)%7

  #compute n 
  n = (h-m+r+90)//25

  #compute p 
  p = (h-m+r+n+19)%32

  #print the result
  month = ""
  if (n==3):
    month = "March"
  if (n==4):
    month = "April"
  print ("In", y, "Easter Sunday is on", p, month+".")
 
#calling main method   
main()