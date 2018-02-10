## prime number game, you have 5 secs to answer - is it a prime number?
import random as rand
import time

yn=0

## start timer
T=time.time()
sec=T
ii=0
score=0
while sec<T+5:
    ## Choose a random integer up to 1000
    num=rand.choice(range(2,1000))
    ## evaluate whether num is prime
    prime=True
    for ii in range(2,num):
        prime=prime and True
        if num%ii==0:
            prime=False
    T=time.time()
    ans=input("Is "+str(num)+" a prime number? y/n: ")
    sec=time.time()
    if prime==True and str(ans)=='y' or prime==False and str(ans)=='n':
        if sec<T+5:
            print(f"Correct! (timing:{round(sec-T,1)} sec)")
            score=score+1
    elif sec>T+5:
        print(f"it took you {round(sec-T,1)} secs, too slow.")
        break
    elif prime==True and str(ans)=='n' or prime==False and str(ans)=='y':
        print(f"wrong, game over.")
        break

print(f"your score is: {score}")
print("try again!")

    
  
































