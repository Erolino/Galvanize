### Rock Paper Scissors game:
### Enter your 'hand' (as string) in the RPS (ROck,Paper,Scissors) function
import random as rand
hand=['Rock','Paper','Scissors']

def RPS(myhand,hand=['Rock','Paper','Scissors']):
    bothand=rand.choice(hand)
    print("bot hand is",bothand)
    u=set([bothand,myhand])
    if myhand==bothand:
        print("Tie of "+myhand+"s.")
        return "Play again"
    elif u.issubset({"Rock","Scissors"}):
        print("Rock beats Scissors")
        if myhand=="Rock":
            print("You win")
        elif bothand=="Rock":
            print("Bot wins")
    elif u.issubset({"Rock","Paper"}): 
        print("Paper beats Rock")
        if myhand=="Paper":
            print("You win")
        elif bothand=="Paper":
            print("Bot wins")
    elif u.issubset({"Paper","Scissors"}):
        print("Scissors beat Paper")
        if myhand=="Scissors":
            print("You win")
        elif bothand=="Scissors":
            print("Bot wins")
