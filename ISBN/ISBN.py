#  File: ISBN.py
 
#  Description: This program confirms the validity of ISBN numbers in a text file. 
 
#  Student Name: Bella Shah
 
#  Date Created: 10/20/2015
 
#  Date Last Modified: 10/21/2015

#Function finds partial sum of the digits of the ISBN number
def partial_sums(sum1):
  s1 = 0
  s1_list = []
  for item in range(len(sum1)):
  	s1 += int(sum1[item])
  	s1_list.append(s1)
  return s1_list

#Function finds the partial sum of s1(partial sum of the partial sum of the ISBN digits)
def partial_sums_s1(sum2):
  s2 = 0 
  s2_list = []
  for item2 in range(len(sum2)):
    s2 += int(sum2[item2])
    s2_list.append(s2)
  return s2

def main():
  # Open file for reading and adds isbn number to list  
  in_file =  open ("./isbn.txt", "r")
  isbn_nums = []
  for line in in_file:  
  	line = line.rstrip()
  	isbn_nums.append(line)
  print (isbn_nums)

  #Creates and opens a new a file to write the output 
  isbnOut = open ("./isbnOut.txt", "w")

  for isbn in range (len(isbn_nums)):
    
    isbn_line = isbn_nums[isbn]
    
    #Prints given ISBN number in isbnOut file
    isbnOut.write(isbn_line)

    #Make ISBN uppercase 
    isbn_nums[isbn] = isbn_nums[isbn].upper()

    #Creates list of ISBN components 
    upper_isbn = list(isbn_nums[isbn])
    
    #Removes hyphen(s) from ISBN number
    for pos in upper_isbn:
      if pos == "-":
        clean_isbn = upper_isbn.remove ("-")
    clean_isbn = upper_isbn
    length_isbn = len(clean_isbn)

    #Checks for length of ISBN number 
    if (length_isbn != 10):
      isbnOut.write("  invalid\n")
      continue 

    #Checks the prescense and postion of letter X in ISBN number
    #Removes X if at the end of ISBN and replaces it with "10"
    if "X" in clean_isbn:
      index_of_x = (clean_isbn.index("X"))
      if (index_of_x != length_isbn-1):
        isbnOut.write("  invalid\n")
        continue
      remove_X = clean_isbn.remove("X")
      remove_X = clean_isbn
      times_ten = remove_X.insert(index_of_x ,'10')

    perm_list = clean_isbn
    print(perm_list)

    #Uses functions created above to check if the last number of the element in s2 is divisible by 11
    #Prints output as valid or invalid
    if partial_sums_s1(partial_sums(perm_list)) % 11 == 0:
      isbnOut.write("  valid\n")
    else:
      isbnOut.write("  invalid\n")
  
  #Closes files 
  in_file.close()
  isbnOut.close()

main()