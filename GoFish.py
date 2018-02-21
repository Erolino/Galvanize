"""Using your Card and Deck class (and any other class you care to implement), make a game of Go Fish playable by two human players. 
(Obviously, this is not ideal, because the two players will be able to see each others cards! Still, we will push on..)

The rules:

Four cards of the same face value are known as a "book"
Five cards are dealt from a standard 52-card deck to each player. The remaining cards are kept in a pile referred to as the "ocean" or "pool"

The player whose turn it is to play asks another player for his or her cards of a particular face value. 
For example Alice may ask, "Bob, do you have any threes?" Alice must have at least one card of the rank she requested.
Bob must hand over all cards of that rank if he has any. 
If he has none, Bob tells Alice to "go fish" and Alice draws a card from the pool and places it in her own hand, ending her turn. Then it is the next player's turn 
When any player at any time has all four cards of one face value, it forms a book, and the cards must be placed face up in front of that player.

When all sets of cards have been laid down in books, the game ends. The player with the most books wins"

"""
os.chdir('/Users/Eran/Galvanize') 
exec(open("./carddeck.py").read())


####Setting up####
# use 'deck class' (from carddeck.py) to create Deck:
d=deck()
deck1=d.create()
# shuffle deck:
deck1=d.shuf()
# creating empty (dictionary) hands
hand1=d.hand()
hand2=d.hand()
# Players choose cards:
   # player 1 alternately player 2
for ii in range(1,11):
    if ii%2!=0:
        pick=d.pick()
        pickstr=str(pick[0])
        val=pickstr.split(" ")[0]
        if hand1[val]==None:
            hand1[val]=pickstr
        elif hand1[val]!=None:
            hand1[val]=[hand1[val],pickstr]
    if ii%2==0:
        pick=d.pick()
        pickstr=str(pick[0])
        val=pickstr.split(" ")[0]
        if hand2[val]==None:
            hand2[val]=pickstr
        elif hand2[val]!=None:
            hand2[val]=[hand2[val],pickstr]
    pool=pick[1]

# Display hands
print("hand1:")
for key in hand1:
    if hand1[key]!=None: print(str(hand1[key]))
print("hand2:")
for key in hand2:
    if hand2[key]!=None: print(str(hand2[key]))
## if you want to print the pool:
print("Pool:")
for ii in range(len(pool)):
    print(pool[ii])

##### Start playing###

#### alternating turns:
for ii in range(1,20):
    if ii%2!=0:
        ans=input("player 1, what card do you want from player 2?:")
    elif ii%2==0:
        ans=input("player 2, what card do you want from player 1?:")

### Algorithm of picking up cards from opponent or pool:
if hand2[ans]!=None:  
    if type(hand1[ans])==list:
        lis=hand1[ans]
        lis.append(hand2[ans])
        hand1[ans]=lis
        hand2[ans]=None
    elif type(hand2[ans])==str and type(hand1[ans])==str:
        hand1[ans]=[hand1[ans]]+[hand2[ans]]
        hand2[ans]=None
    elif type(hand2[ans])==list and type(hand1[ans])==str:
        lis=hand2[ans]
        lis.append(hand1[ans])
        hand1[ans]=lis
        hand2[ans]=None
elif hand2[ans]==None: 
    #pick up from pool:
    Cardandpool=d.pick()
    Pool=Cardandpool[1]
    card1=Cardandpool[0]
    card1str=str(Cardandpool[0])
    card1splitVal=card1str.split(" ")[0]
    if hand1[card1splitVal]==None:
        hand1[card1splitVal]=card1str
    elif hand1[card1splitVal]!=None:
        if type(hand1[card1splitVal])==list:
            liss=hand1[card1splitVal]
            liss.append(card1str)
            hand1[card1splitVal]=liss
            ## hand1[card1splitVal]=[hand1[card1splitVal],card1str]
        elif type(hand1[card1splitVal])==str:
            hand1[card1splitVal]=[hand1[card1splitVal]]+[card1str] 
    
print("hand1:")
for key in hand1:
    if hand1[key]!=None: print(str(hand1[key]))
print("hand2:")
for key in hand2:
    if hand2[key]!=None: print(str(hand2[key]))           
        
### Checking if there are complete sets
table1={}
for key in hand1:
    if hand1[key]!=None:
        if len(hand1[key])==4:
            table1[key]=hand1[key]
print("Player 1 sets: "+str(table1))
### If there are more than 6 sets for one player - he wins
if len(table1)>6:
    print("Player 1 has more than half of the sets.. Player 1 wins!")
    
 


    
     


