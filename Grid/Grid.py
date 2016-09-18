#  File: Grid.py

#  Description: This program find the greatest product of four adjacent numbers in the same direction (horizontal, vertical, or diagonal) in a grid of positive integers

#  Student Name: Bella Shah

#  Date Created:10/27/2015

#  Date Last Modified: 10/28/2015

#Finds the maximum product of the columns
def prod_cols (b):
  max_prod_cols = 0
  for i in range(len(b)):                 
    for j in range(len(b[i])-3):       
      column = (b[i][j])*(b[i][j+1])*(b[i][j+2])*(b[i][j+3])
      if column > max_prod_cols:
        max_prod_cols = column
  return max_prod_cols
 
#Finds the maximum product of the rows
def prod_rows (b):     
  max_prod_rows = 0
  limit = len(b[0])-3
  for i in range(limit):     
    for j in range(len(b)):
      row = (b[i][j])*(b[i+1][j])*(b[i+2][j])*(b[i+3][j])
      if row > max_prod_rows:
        max_prod_rows = row
  return max_prod_rows

#Finds the maximum product of the diagonal from right to left
def prod_rl (b):       
  max_prod_rl = 0
  limit = len(b[0])-3
  for i in range(limit):        
    for j in range(len(b[i])-3):
      diagonal = (b[i][j])*(b[i+1][j+1])*(b[i+2][j+2])*(b[i+3][j+3])
      if diagonal > max_prod_rl:
        max_prod_rl = diagonal
  return max_prod_rl

#Finds the maximum product of the diagonal from left to right
def prod_lr (b):             
  max_prod_lr = 0
  for i in range(3,len(b)):           
    for j in range(len(b[i])-3):
      diagonal = (b[i][j])*(b[i-1][j+1])*(b[i-2][j+2])*(b[i-3][j+3])
      if diagonal > max_prod_lr:
        max_prod_lr = diagonal
  return max_prod_lr     

def main():
  # open file for reading
  in_file = open ("./grid.txt", "r") 

  # read the dimension of the grid
  dim = in_file.readline()
  dim = dim.strip()
  dim = int (dim)

  # create a 2-D list
  grid = []
  max_prod = 0

  # read data line by line
  for i in range (dim):
    line = in_file.readline()
    line = line.strip()

    # split the line
    nums = line.split()

    # convert into integers
    for j in range (dim):
      nums[j] = int (nums[j])

    # append nums to the 2-D list
    grid.append (nums)

  #Finds the max product of the rows, columns and diagonals
  max_prodFinal = max(prod_rows(grid),prod_cols(grid),prod_lr(grid),prod_rl(grid))

  #Prints output
  print ("The greatest product is "+str(max_prodFinal) + ".")

  # close file
  in_file.close()

main()