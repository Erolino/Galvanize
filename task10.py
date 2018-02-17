## Problem 1

def max_lists(list1,list2):
    maxx=[]
    for ii in range(len(list1)):
        if list1[ii]>list2[ii]:
            maxx.append(list1[ii])
        else:
            maxx.append(list2[ii])
    return maxx

## Problem 2

# e.g. input mat=[[2,3],[5,6],[10,11]]

def get_diagonal(mat):
    if len(mat)>len(mat[0]):length=len(mat[0])
    else:length=len(mat)
    output=[]
    for ii in range(length):
        output.append(mat[ii][ii])
    return output



