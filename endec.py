## A function that takes a word, asks if you'd like to decode or encode depnded on built in rules:
## a is b, b is c and so on..

def endec(word):
    Method = input('If you would like to encode, type: E, if to decode, type D:')
    ## making the dictionary:
    import string
    alpha=string.ascii_lowercase
    beta=string.ascii_lowercase[1:-1]+"z"+"a"
    encode={}
    decode={}
    for ii in range(0,len(alpha)):
        encode[alpha[ii]]=beta[ii]
        decode[beta[ii]]=alpha[ii]
    ## Making the new word:
    newword=str()
    for jj in range(0,len(word)):
        let=word[jj]
        if Method=="E":
            newword=newword+encode[let]
        elif Method=="D":
            newword=newword+decode[let]
    return newword
            
        








