"""The Birthday Problem.  Suppose there are 23 people in a data science class, lined up 
in a single file line. Let A_i be the event that the i'th person doesn't have the same 
birthday as the j'th person for any j < i.  Use the chain rule from probability to calculate 
the probability that at least 2 people share the same birthday.
"""

# birthday prob = 1/365
# any combination of 23 birthdays would be: (1/365)^23
# E(i) is an event where person i's (i=range(0,22) birthday is different than person's j= range(1,23)
# p(E1,E2,...,E23) where distinct is the complementing where there is at least one pair= 1-p
# 364/365*363/365*362/365

def sameBday(class_size=23):
    pno=1
    for i in range(1,class_size+1):
        pno=pno*(365-i)/365
    pno
    print(f"the chance of having at least 2 identical birthdays in a {i} student class is {100*round(1-pno,2)}%")
    
        
