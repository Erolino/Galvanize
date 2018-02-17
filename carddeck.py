# Task #9 for beginning of Monday's class. Design a Python class called Card, and then  a Python class called Deck 
# that represents a deck of cards. The cards should have four suits (hearts spades clubs and diamonds) and go from 2 to Ace like 
# normal playing cards. 

# Make a list of attributes and methods that your Card and Deck classes should have, and implement them as time permits.

from random import shuffle
from random import choice

class card():
        
    def __init__(self, suite, value):
            self.suite = suite
            self.value = value

    def __str__(self):
            return "{} of {}".format(self.value,self.suite)
class deck():
            
    def __init__(self):
        self.create()
        self.shuf()
        self.choice(top=True)
        
    def create(self,numOFdeck=1):
        suites=['spades','hearts','clubs','diamonds']
        listall=[]
        for elem in suites:
            for ii in range(2,15):
                card.suite=elem
                if ii==11: ii='jack'
                elif ii==12:ii= "queen"
                elif ii==13:ii='king'
                elif ii==14:ii='ace'
                card.value=str(ii)
                print("{} of {}".format(card.value,card.suite))
                listall.append(card(card.suite,card.value))
        print(len(listall))
        self.decks=listall*numOFdeck
        return self.decks
    
    def shuf(self):
        shuffle(self.decks)
        return(self.decks)
        
    def __str__(self):
            return "{}".format(self.decks)
        
    def choice(self,top=True):
        if top==True:
            card=self.decks[0]
        else:
            card=choice(self.decks)
        return(card)
            
            
    
# ##### code ####
# ## Create an instance:
# d1=deck()
# ## to create a deck:
# deck.create(d1)
# ## to choose a random card from deck created:
# rand=deck.choice(d1,top=False)
# print(rand) ## to see the choice
# ## to choose from top:
# top=deck.choice(d1)
# print(top)
# ####### ########


        




