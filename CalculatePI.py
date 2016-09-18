
#  File: CalculatePI.py

#  Description: This program calculates PI using random numbers and finds the difference between the real value of PI and Calculated PI. 

#  Student Name: Bella Shah

#  Date Created: October 2, 2015

#  Date Last Modified: October 16, 2015

#Function that computes PI based on the number of throws on a random point on a dart board
def computePI (numThrows):
  import random
  import math
  numHits = 0

  for i in range(numThrows):
    xPos = random.uniform (-1.0 , 1.0)
    yPos = random.uniform (-1.0 , 1.0)
    if math.hypot(xPos, yPos) < 1:
    	numHits += 1
  pi = 4 * numHits/numThrows 
  return pi 

#Calls function computePI() for specified number of darts 
#Prints calculated PI and the difference between true PI and calculated PI for various number throws.  
def main ():
  import math
  #Initialized variables for Calculated PI and Difference
  #Ensures computePI() was not computing two different random numbers for calculated PI and difference. 
  Num1 = computePI(100)
  Diff1 = Num1 - math.pi
  Num2 = computePI(1000)
  Diff2 = Num2 - math.pi
  Num3 = computePI(10000)
  Diff3 = Num3 - math.pi
  Num4 = computePI(100000)
  Diff4 = Num4 - math.pi
  Num5 = computePI(1000000)
  Diff5 = Num5 - math.pi
  Num6 = computePI(10000000)
  Diff6 = Num6 - math.pi

  print ("Computation of PI using Random Numbers")
  print ("")
  print ("num = 100","        Calculated PI = ",format(Num1,".6f"),"   Difference = ", format(Diff1,"+.6f"))
  print ("num = 1000","       Calculated PI = ",format(Num2,".6f"),"   Difference = ", format(Diff2,"+.6f"))
  print ("num = 10000","      Calculated PI = ",format(Num3,".6f"),"   Difference = ", format(Diff3,"+.6f"))
  print ("num = 100000","     Calculated PI = ",format(Num4,".6f"),"   Difference = ", format(Diff4,"+.6f"))
  print ("num = 1000000","    Calculated PI = ",format(Num5,".6f"),"   Difference = ", format(Diff5,"+.6f"))
  print ("num = 10000000","   Calculated PI = ",format(Num6,".6f"),"   Difference = ", format(Diff6,"+.6f"))
  print ("")
  print ("Difference = Calculated PI - math.pi")
main()