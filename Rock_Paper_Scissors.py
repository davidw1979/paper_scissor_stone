#Rock Paper Scissors Game

from random import randint

#Winning functions
def youwin(user_sel):
    print ("You win")
    return

def comwin(user_sel):
    print ("Computer wins")
    return

#Results functions
def rockvspaper(user_sel):
    print ("PAPER covers ROCK")
    if user_sel == "P":
        youwin(user_sel)
        return
    else:
        comwin(user_sel)
        return
    
def rockvsscissors(user_sel):
    print ("ROCK smashes SCISSORS")
    if user_sel == "R":
        youwin(user_sel)
        return
    else:
        comwin(user_sel)
        return

def papervsscissors(user_sel):
    print ("SCISSORS cuts PAPER")
    if user_sel == "S":
        youwin(user_sel)
        return
    else:
        comwin(user_sel)
        return

#Set up choices list
choices = ["ROCK", "PAPER", "SCISSORS"]

#Get user_sel, slice first letter & convert to upper case
user_sel = input("What do you choose Rock(R), Paper(P) or Scissors(S)? ")
user_sel = user_sel[:1].upper()

#Check user_sel against R,P,S and print weapon choice   
if user_sel == "R": 
    print ("You have selected ROCK")

elif user_sel == "P":
    print ("You have selected PAPER")
    
elif user_sel == "S":
    print ("You have selected SCISSORS")  

else:
    print ("You have failed to pick a weapon!!!")
   
#Generate computer selection store R,P,S as com_sel and print
com_num = randint(0,2)
com_sel = choices[com_num][:1]
print ("Computer selects " + choices[com_num])

#Draw game
if user_sel == com_sel:
    print ("Match drawn...")

#Call appropriate results function
elif user_sel + com_sel == "PR" or user_sel + com_sel == "RP":
    rockvspaper(user_sel)

elif user_sel + com_sel == "SR" or user_sel + com_sel == "RS":
    rockvsscissors(user_sel)

elif user_sel + com_sel == "PS" or user_sel + com_sel == "SP":
    papervsscissors(user_sel)

else:
    comwin(user_sel)
