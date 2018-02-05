### hangman.
### 1st make sure this file and the file of words are saved in the same folder

def oneW(letter,word,sentlist):
    empty=True
    for ii in range(0,len(word)):
        if word[ii]==letter:
            sentlist[ii]=word[ii]
            empty=False
    return sentlist,empty

def hangman(name_of_file):
    ## read in the file, e.g. "What.txt":
    uuu=open(name_of_file,"r")
    words=uuu.read()
    words=words.lower()
    ## creating spaces:
    ## sentence=words.replace(" ","")
    sentence=list(words.lower())
    
    import string
    alpha=string.ascii_lowercase  
    ## This prints out the sentence in "stars"
    for x in range(0,len(words)):
        if sentence[x] in alpha: 
            sentence[x]='*'
    
    sentlist=sentence ## starts list
    print("Let's start guessing. Your sentence is:") 
    phrase=" ".join(sentence)
    print(phrase) ## Prints out the unrevealed sentence
    
    
    wordlist=list(words) ##revealed letter list
    ## the sentece to guess is: words
    ## the intial output the user sees: sentence
    ## Set the number of guesses according to length of words
    
    char=len(list(words))
    wordlis=words.split(" ")
    totlet=char-len(wordlis)
    guesses=totlet
    if guesses>15:
        guesses=15
    
    while guesses > 0:
        print("you got "+str(guesses)+" guesses")
        let = input('What is your guess: ')
        TF=True
        out=oneW(let,words,sentlist)
        revealed=out[0]
        print(" ".join(revealed))
        TF=TF and out[1]
        if TF==True: 
            guesses=guesses-1
            print("Nope, try again")
        elif TF==False: print("good guess!")
        if "*" not in revealed: 
            print("Great Job, you win!")
            break
    if guesses==0: print("Sorry you lose!") 
    
hangman('What.txt')

    


