#  File: DNA.py

#  Description: This program finds the common substrand(s) between 2 DNA strands. 

#  Student Name: Bella H Shah

#  Date Created: 10/09/2015

#  Date Last Modified: 10/12/2015
def main():

  # Open file for reading
  in_file =  open ("./dna.txt", "r")

  # Read number of pairs
  num_pairs = in_file.readline()
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)
 
  print ("Longest Common Sequences", "\n")
  
  # Read each pair of dna strands   
  for i in range (num_pairs):
    st1 = in_file.readline()
    st2 = in_file.readline()

    # Remove white space from either end
    st1 = st1.strip()
    st2 = st2.strip()

    # Make both strands upper case
    st1 = st1.upper()
    st2 = st2.upper()

    # Order strands by size
    if (len(st1) > len(st2)):
      dna1 = st1
      dna2 = st2
    else:
      dna1 = st2
      dna2 = st1 
    
    #Get all substrings of dna2
    wnd = len (dna2)
    longest_strand = 0
    Common_Strand = []
    while (wnd > 1):
      start_idx = 0
      while ((start_idx + wnd) <= len (dna2)):
        sub_strand = dna2[start_idx: start_idx + wnd] #Finds all substrands of dna2
        start_idx += 1
        print (sub_strand) # Move starting place by 1
        # Determine if substrand(s) of dna2 are in dna1 and finds longest common substrand between dna1 and dna2. 
        if (sub_strand in dna1):
          strand_len = len(sub_strand.strip())
          if (strand_len >= longest_strand):
            longest_strand = strand_len
            if (sub_strand not in Common_Strand): # Only adds common substrand to list once. Avoids duplicate common substrands. 
              Common_Strand.append(sub_strand) #Extra Credit

      # Decrease window size
      wnd = wnd - 1

    # Prints and formats result
    print ("Pair", str( i + 1) + ": ", end = "") 
    if (len(Common_Strand) == 0):
      print ("No Common Sequence Found")
      print ("")
    else:
      print (Common_Strand[0])
      for i in range (1 ,len(Common_Strand)):
        print ("        " + Common_Strand[i])
      print ("")

  # Close file
  in_file.close()

main()