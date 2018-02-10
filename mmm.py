Task 8 - Mean, Median, and Mode (Computed From Scratch)

1) Write a function that, given an arbitrary list of numbers (or a range, or a tuple of numbers) computes the mean.

2) Write a function that, given an arbitrary list of numbers (or a range of numbers, or a tuple of numbers) computes the median.
# median func:
## obtains the data
   
# e.g. inputs: 
# lis=[1,2,3,4]
# tup=(1,4,6)
# ran=range(1,12)

def median(data):
    ## turns everything to a specific type - list
    datalis =list(data)
    ## medean algorthm:
    leng=len(datalis)
    if leng%2!=0:
        ans=datalis[round(leng/2)-1]
    elif leng%2==0:
        ans=(datalis[int(leng/2-1)]+datalis[int(leng/2)])/2
    return ans


3) Write a function that, given an arbitrary list of numbers (or a range, or a tuple of numbers) computes the mode.

see docstring below for examples
"""
list1 = [2,3,4]
>>> mean(list1) = 3
>>> median(list1) = 3
>>> mode(list1) = None

list2 = [10,1,4,3,2,10]
>>> mean(list2) = 5
>>> median(list2) = 3.5
>>> mode(list2) = 10

range1 = range(2,5)
>>> mean(range1) = 3
>>> median(range1) = 3
>>> mode(range1) = None

range2 = range(1,101)
>>> mean(range2) = 5050
>>> median(range2) = 50.5
>>> mode(range2) = None


tuple1 = (10,4,6,8,2)
>>> mean(tuple1) = 6
>>> median(range1) = 6
>>> mode(range1) = None

tuple2 = (10,4,6,8,2,10000,4)
>>> mean(tuple1) = 1433.4 
>>> median(range1) = 6
>>> mode(range1) = 4
"""