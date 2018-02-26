"""Google decides to do random drug tests for heroin on their employees. 
They know that 3% of their population uses heroin. The drug test has the following 
accuracy: The test correctly identifies 95% of the heroin users (sensitivity) and 
90% of the non-users (specificity).

             Uses heroin	Doesn't use heroin
Tests positive	0.95	0.10
Tests negative	0.05	0.90

Alice gets tested and the test comes back positive. What is the probability 
that she uses heroin?"""

#   TP=0.95 -> Sensitivity
#   TN=0.05
#   FN=0.9 -> Specificity
#   FP=0.1
#   PR = 0.03 -> PopulationRate

def DrugTest(Sensitivity,Specificity,PopulationRate):

    TP=Sensitivity # p(Positive / True) 
    TN=1-TP  # p (Negative / True)
    FN=Specificity  # p(Negative / False)
    FP=1-FN  # p(Positive / False)
    ##
    T=PopulationRate
    
    # p(True / Positive)=?
    # [1] p(True / Positive)= p(Positive / True)*  p(True)
    #                     ------------------------------
    #                           p(positive)
    # What is missing in the formula to get the answer is p(positive). 
    P=0
    #so we'll switch it to:
    # p(positive)= p(positive / True)*p(True) + p(positive / False)*p(False):
    P=TP*T+FP*(1-T)
    ans=TP*T/P  # from [1]
    print(f"employee has {round(ans,2)*100}% chance to be a drug user if tested positive")
    
DrugTest(.95,.9,0.03)
    
    




