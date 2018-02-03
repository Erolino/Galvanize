### Rock Paper Scissors game:
### Enter your 'hand' (as string) in the RPS (ROck,Paper,Scissors) function
import random as rand
## Choose your hand: 'Rock','Paper','Scissors','Lizard' or 'Spock'

def RPSLS(myhand,hand=['Rock','Paper','Scissors','Lizard','Spock']):
    bothand=rand.choice(hand)
    print("bot hand is",bothand)
    dict={'Spock':['Rock','Scissors'],'Lizard':['Paper','Spock'],'Paper':["Rock","Spock"],"Rock":["Lizard","Scissors"],"Scissors":["Lizard","Paper"]}
    if myhand=='Spock':
        if bothand in dict["Spock"]: print("Spock beats "+str(bothand)+", you win")
        elif myhand=='Spock' and bothand=='Spock': print("Tie, play again")
        else: print("Spock loses to "+str(bothand)+", bot wins")
    elif myhand=='Lizard':
        if bothand in dict["Lizard"]: print("Lizard beats "+str(bothand)+", you win")
        elif myhand=='Lizard' and bothand=='Lizard': print("Tie, play again")
        else: print("Lizard loses to "+str(bothand)+", bot wins")
    elif myhand=='Paper':
        if bothand in dict["Paper"]: print("Paper beats "+str(bothand)+", you win")
        elif myhand=='Paper' and bothand=='Paper': print("Tie, play again")
        else: print("Paper loses to "+str(bothand)+", bot wins")
    elif myhand=='Rock':
        if bothand in dict["Rock"]: print("Rock beats "+str(bothand)+", you win")
        elif myhand=='Rock' and bothand=='Rock': print("Tie, play again")
        else: print("Rock loses to "+str(bothand)+", bot wins")
    elif myhand=='Scissors':
        if bothand in dict["Scissors"]: print("Scissors beats "+str(bothand)+", you win")
        elif myhand=='Scissors' and bothand=='Scissors': print("Tie, play again")
        else: print("Scissors loses to "+str(bothand)+", bot wins")






