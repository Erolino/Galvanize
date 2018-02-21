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

class deck(card):
            
    def __init__(self):
        self.decks=[]
        pool=[]
        
    def create(self,numOFdeck=1):
        suites=['spades','hearts','clubs','diamonds']
        listall=[]
        dic={}
        for elem in suites:
            for ii in range(2,15):
                card.suite=elem
                if ii==11: ii='jack'
                elif ii==12:ii= "queen"
                elif ii==13:ii='king'
                elif ii==14:ii='ace'
                card.value=str(ii)
                dic[card.value]=card.value
                listall.append(card(card.suite,card.value))
        self.decks=listall*numOFdeck
        return self.decks,dic
    
    def shuf(self):
        shuffle(self.decks)
        return(self.decks)
        
    def __str__(self):
        return "{} of {}".format(card.value,card.suite)
        
    def pick(self):
        if len(self.decks)==0:
            print("no more crads in pool")
        card=self.decks[0]
        del(self.decks[0])
        return card,self.decks
        
    def hand(self):
        handd={}
        for ii in range(2,15):
            if ii==11: ii='jack'
            elif ii==12:ii= "queen"
            elif ii==13:ii='king'
            elif ii==14:ii='ace'
            card.value=str(ii)
            handd[card.value]=None
        return handd
            








