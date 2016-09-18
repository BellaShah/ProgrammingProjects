#  File: Day.py

#  Description: This program returns the day of the week for any date between 1900 and 2100. 

#  Student Name: Bella Shah

#  Date Created: September 14, 2015

#  Date Last Modified: September 16, 2015

def main ():
  
  #Prompts the user to enter year between 1900 and 2100
  year = int (input("Enter year: "))
  while ((year<1900) or (year>2100)):
  	year = int (input ("Enter year: "))
  
  #Prompts the user to enter month between 1 and 12
  month = int (input("Enter month: "))
  while ((month<1) or (month>12)):
    month = int (input ("Enter month: "))
  
  #Checks to see if year is a leap year  
  is_leap = (year%400==0) or ((year%100!=0) and (year%4==0))

  #Converts input month number to month number that corresponds with program
  if (month<3):
    a = month+10
  else:
    a = month-2
  if ((month==1) or (month==2)):
    year = year-1 

  #Prompts the user to enter day for specific month and check to see if number of days are in specified month.
  day = int (input("Enter day: "))
  while ((a==1 or a==3 or a==5 or a==6 or a==8 or a==10 or a==11) and (day>31 or day<1)):
    day = int(input("Enter day: "))
  while ((a==2 or a==4 or a==7 or a==9) and (day>30 or day<1)):
    day = int(input("Enter day: "))
  if (a==12):
    while ((day>28 or day<1) and not is_leap) or ((day>29 or day<1) and is_leap):
      day = int(input("Enter day: "))
  
  #Computes day of the week 
  b = day
  c = year%100
  d = year//100
  w = (13*a-1)//5
  x = c//4
  y = d//4
  z = w+x+y+b+c-2*d
  r = z%7
  r = (r+7)%7

  #Prints result 
  if(r==0):
    print("The day is Sunday.")
  if(r==1):
    print("The day is Monday.")
  if(r==2):
    print("The day is Tuesday.")
  if(r==3):
    print("The day is Wednesday.")
  if(r==4):
    print("The day is Thursday.")
  if(r==5):
    print("The day is Friday.")
  if(r==6):
    print("The day is Saturday.")

main()