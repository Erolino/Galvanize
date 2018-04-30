# The bus problem:
# https://www.stat.auckland.ac.nz/~brewer/stats331.pdf

# A) Repeat the bus example from the stats331 handout, but use a grid of 101 evenly spaced points between 0 and 1, inclusive.

# B) Suppose the professor tries again. For the following 7 days, he only gets to his job correctly 1 time.
# Using your answer from A), find the new posterior distribution.

# C) Using B, predict the probability he gets the correct bus on the *next* day after his 7 day streak.
# see section 4.2 in stats331 notes.

'A)'
# create a 'Bayes Box'
param<-seq(0,1,1/100) # this is the possible parameters values for our model (0 to 1
# cause its probabilities) we chise 100 different probabilities just because. 
# we want to choose the best parameter (with the highest probability to predict the data)
numparam=length(param) 
prior=rep(1/numparam,101) # we use prior that is unified distribution (cause we don't really have info on the busses)
## A function that creates a bayes table. the model we chose for liklihood is binomial:
bayestable=function(paramet,priors,success,N){
  df=data.frame(parameters=paramet,prior=priors)
  ## the success (random variable value) out of 5 attempts (this is the 1st data that
  # allows us to makeup the liklihood)
  ## so what's its probability? use binomial distribution because it's success failure type 
  # let's use: dbinom(k,n,p) for every probability which in our case is the 100 different oparametrs
  liklihood=dbinom(success,N,paramet)
  pXl=prior*liklihood
  post=pXl/sum(pXl)
  df=data.frame(df,liklihood=liklihood,prior_x_liklihood=pXl,posterior=post)
  return(df)
}
DF=bayestable(param,prior,2,5) ## first data input: 2 sucesses out of 5
plot(DF$parameters,DF$prior,ylim = c(0,0.035),xlab = 'parameter',ylab = 'probability')
par(new=T)
legend(0.6,0.02,legend = 'prior (no knowledge)',box.lty=0)
par(new=T)
plot(DF$parameters,DF$posterior,ylim = c(0,0.035),xlab = '',ylab = '',col='blue')
legend(0.58,0.028,legend = 'posterior#1 for 2 in 5',box.lty=0,text.col = 'blue')
'B)'
## new data is 1 success out of 7 attempts, let's update the table and find new poterior
DF=bayestable(param,DF$posterior,1,7) 
par(new=T)
plot(DF$parameters,DF$posterior,ylim = c(0,0.035),xlab = '',ylab = '',col='brown')
par(new=T)
legend(0.58,0.036,legend = 'posterior#2 for 1 in 7',box.lty=0,text.col = 'brown')
'C)'
ind=which(DF$posterior==max(DF$posterior)) ## the distribution for the prob for parameters success 
maxlikly=DF$parameters[ind] ## The most likly (highest probability) parameter (probability) for being succesful with a bus 




