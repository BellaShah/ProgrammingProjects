#  File: GuessingGame.py

#  Description: TIn this program you will prompt the user to think of a number between 1 and 100. Your program will make a guess what the number is.

#  Student Name: Bella Shah

#  Date Created:11/01/2015

#  Date Last Modified: 11/01/2015
def main():
    #Print header
    print("Guessing Game\n""\n"
        "Think of a number between 1 and 100 inclusive.\n"
        "And I will guess what it is in 7 tries or less.\n")
    
    #Prompts user to enter y or n to begin game
    YorN = str(input ("Are you ready? (y/n): "))
    print ("")
    
    #Error checks prompt and reprompts user for appropriate response
    while (YorN != "y" and YorN != "n"): 
        YorN = str(input ("Are you ready? (y/n): "))
        print("")

    #Checks if user is ready to play the game 
    if YorN == "y":
        lo, hi = 1, 100
        answer = False
        #Binary Search algorithm
        for tries in range(1, 8):
            mid = (lo + hi) // 2
            print("Guess ", tries,":  The number you thought was",mid) 
            #Prompts user to enter whether guess was too high, low or correct
            Check = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")) 
            print ("")
            #Error checks the Check prompt
            while (Check != -1 and Check != 1 and Check != 0): 
                print("Guess ", tries,":  The number you thought was",mid)
                Check = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
                print("")
            #Alters the search window based on user response           
            if Check == -1:
                lo = mid + 1
            elif Check == 1:
                hi = mid - 1
            else:
                answer = True
                break
            if lo > hi:
                break
        if answer == True:
            print("Thank you for playing the Guessing Game.")
        else:
            print("Either you guessed a number out of range or you had an incorrect entry.")
    elif YorN == "n":
        print("Bye!")
main()  