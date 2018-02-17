#max_lists(list1,list2)
list1=[1,2,3]
list2=[-1,4,2]
maxx=[]
for ii in range(len(list1)):
    if list1[ii]>list2[ii]:
        maxx.append(list1[ii])
    else:
        maxx.append(list2[ii])
maxx
    

