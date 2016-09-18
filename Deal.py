#  File: Deal.py

#  Description: This program simulates Let's Make a Deal gameshow and tries to prove Marilyn vos Savants advice about taking the switch when offered increased probability of winning. 

#  Student Name: Bella Shah

#  Date Created: October 6, 2015

#  Date Last Modified: October 7, 2015

def main():
  import random
  #Prompts the user to enter number of times they want to play and error checks that number
  num_trials = int (input("Enter number of times you want to play: "))
  while (num_trials < 1):
    num_trials = int (input("Enter number of times you want to play: "))

  #Initialize variable to count number of trials and count number of wins that occur due to a switch
  trial = 0
  switch = 0
  
  #Goes through each trial to randomly determine which door has the prize, the guess, and the newGuess.
  #Determines if the newGuess is the same as the prize behind the door, if so, a win for switching increases. 
  #Prints door with the prize, the contestant's guess, the door with no prize, and the new guess.     
  print ("")
  print ("  Prize      Guess       View    New Guess")
  while (trial < num_trials ):
    prize = random.randint(1,3)
    guess = random.randint(1,3)
    view = random.randint(1,3)
    newGuess = random.randint(1,3)
    while (view == guess or view == prize ):
      view = random.randint(1,3)
    while (newGuess == view or newGuess == guess):
      newGuess = random.randint(1,3)
    if (newGuess == prize):
      switch += 1
    trial += 1
    print ("   ",prize,"        ",guess,"        ",view,"        ",newGuess)

  #Determines probability of winning from switching your guess and winning from not switching your guess
  SwitchWin = switch / num_trials
  noSwitchWin = 1 - SwitchWin

  #Prints probability of winning with switching guesses and winning without switching guesses
  print ("")
  print ("Probability of winning if you switch = ",format(SwitchWin,".2f"))
  print ("Probability of winning if you do not switch = ",format(noSwitchWin,".2f")) 

main()