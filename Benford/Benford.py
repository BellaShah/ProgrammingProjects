#  File: Benford.py

#  Description: This program verifies Benford's law for the US Census data of 2009.

#  Student Name: Bella H Shah

#  Date Created: 11/23/2015

#  Date Last Modified: 11/23/2015
def main():

#create new, empty dictionary
  pop_freq={}
     
#initialize the dictionary
  for i in range (0,10):
    pop_freq[str(i)] = 0 

#open file for reading
  in_file=open("./Census_2009.txt","r")

# read the header and ignore    
  header=in_file.readline()
     
#read subsequent lines
  for line in in_file:
    line=line.strip()
    pop_data=line.split()
    # get the last element that is the population number
    pop_num=pop_data[-1]
    #splits into each digit on number in a list and find the first digit of the number
    new = list(pop_num)
    first_num = int(new [0])

    #process the data
    for i in range (1,10):
      if first_num == i:
        pop_freq[str(i)]+=1       
         
#finds the total number of people
  totalnumber = 0
  for i in range (1,10):
    totalnumber += pop_freq[str(i)]
  
#print the results
  print ("Digit   Count   %")
  for i in range(1, 10):
    percentage = format(((pop_freq[str(i)]/totalnumber)*100),"0.1f")
    print(i,"       ", str(pop_freq[str(i)]).ljust(8),percentage.ljust(4),sep="")
 
#close file
    in_file.close()
     
main()