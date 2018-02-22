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
# print("Pool:")
# for ii in range(len(pool)):
#     print(pool[ii])


##### Start playing###

ii=0
tableX={}
while len(tableX)<7:
    #### alternating turns:
    print(f"Total number of turns played = {ii}")
    ii=ii+1
    if ii%2!=0:
        x=1
        handX=hand1
        handY=hand2
        ans=input("player 1, what card do you want from player 2?:")
        if handX[ans]==None:
            ans=input("You can't ask for a card you don't have, try again player 1 - ask for a card:")
            if handX[ans]==None:
                print("fooled me once shame on me, fooled me twice shame on you. Game over! player 2 wins. Play fairly next time")
                break
    elif ii%2==0:
        x=2
        handX=hand2
        handY=hand1
        ans=input("player 2, what card do you want from player 1?:")
        if handX[ans]==None:
            ans=input("You can't ask for a card you don't have, try again player 2 - ask for a card:")
            if handX[ans]==None:
                print("fooled me once shame on me, fooled me twice shame on you. Game over! player 1 wins. Play fairly next time")
                break

    ### Algorithm of picking up cards from opponent or pool:
    if handY[ans]!=None:
        #pick up from opponent:
        if type(handX[ans])==list:
            lis=handX[ans]
            lis.append(handY[ans])
            handX[ans]=lis
            handY[ans]=None
        elif type(handY[ans])==str and type(handX[ans])==str:
            handX[ans]=[handX[ans]]+[handY[ans]]
            handY[ans]=None
        elif type(handY[ans])==list and type(handX[ans])==str:
            lis=handY[ans]
            lis.append(handX[ans])
            handX[ans]=lis
            handY[ans]=None
    elif handY[ans]==None: 
        #pick up from pool:
        Cardandpool=d.pick()
        Pool=Cardandpool[1]
        card1=Cardandpool[0]
        card1str=str(Cardandpool[0])
        card1splitVal=card1str.split(" ")[0]
        if handX[card1splitVal]==None:
            handX[card1splitVal]=card1str
        elif handX[card1splitVal]!=None:
            if type(handX[card1splitVal])==list:
                liss=handX[card1splitVal]
                liss.append(card1str)
                handX[card1splitVal]=liss
            elif type(handX[card1splitVal])==str:
                handX[card1splitVal]=[handX[card1splitVal]]+[card1str] 
        
    print("hand1:")
    for key in hand1:
        if hand1[key]!=None and len([hand1[key]])<4:
            print(str(hand1[key]))
    print("hand2:")
    for key in hand2:
        if hand2[key]!=None and len([hand2[key]])<4: 
            print(str(hand2[key]))           
            
    ### Checking if there are complete sets
    for key in handX:
        if handX[key]!=None:
            if len(handX[key])==4:
                tableX[key]=handX[key]
    print(f"Player {x} has {len(tableX)} sets: {tableX}")
    #### show how many cards left in pool:
    print(f"cards left in pool: {len(pool)}")
    ###### Updating hand1 and hand2 according to the changes of this round:
    if x==1: hand1=handX
    if x==2: hand2=handX
    ### If there are more than 6 sets for one player - he wins
    if len(tableX)>6:
        print(f"Player {x} has more than half of the sets.. Player {x} wins!")
        break
    
 
