# Task 5 : 
# Write a function called calculator. 

# It should take the following parameters: 
# A)two numbers, and
# B)an arithmetic operation (which can be addition, subtraction, multiplication or division)


# The function should perform the requested operation on the two input numbers, 
# Raise exceptions as appropriate if any of the parameters passed to the function are invalid.\
# Use enum and/or dictionaries as needed to solve this task

def op(param,oper):
    operations=["Divide","Multiply","Substract","Add"]
    anss=None
    for value in operations:
        if oper==value:
            if value=="Divide":
                if param[1]==0: print("Not alowed")
                else: anss=param[0]/param[1]
            elif value=="Multiply": anss=param[0]*param[1]
            elif value=="Substract": anss=param[0]-param[1]
            elif value=="Add": anss=param[0]+param[1]
    print(anss)
    
            
