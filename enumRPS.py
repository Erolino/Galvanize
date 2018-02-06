import random as rand
import enum

class ropasc(enum.Enum):

    Scissors = 3
    Paper = 2
    Rock = 1

def rocky(myhand):
    myhand="Rock"
    hand=['Rock','Paper','Scissors']
    bothand=rand.choice(hand)
    print("bot hand is",bothand)
    dict={'Rock':ropasc.Rock,'Paper':ropasc.Paper,'Scissors':ropasc.Scissors}
    mine=dict[myhand]
    bots=dict[bothand]
    if mine==bots: 
        print("tie of "+str(mine.name)+", try again")
    elif mine.name=="Rock":
        if bots.name=="Paper": print("Paper beats Rock, you lose!")
        elif bots.name=="Scissors": print("Rock beats Scissors, you win!")
    elif mine.name=="Scissors":
        if bots.name=="Paper": print("Scissors beats Paper, you win!")
        elif bots.name=="Rock": print("Rock beats Scissors, you lose!")
    elif mine.name=="Paper":
        if bots.name=="Scissors": print("Scissors beats Paper, you lose!")
        elif bots.name=="Rock": print("Paper beats Rock, you win!")





