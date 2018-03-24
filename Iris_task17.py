#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:14:07 2018

@author: eran
"""
import numpy as np
import pandas as pd

"""### let's import the data ##"""
from sklearn import datasets
from sklearn.model_selection import train_test_split 

iris = datasets.load_iris()
list(iris.keys()) #"it's not a DF so need to use keys"
print(iris.DESCR) #"A description"

iris.feature_names # names of varuables (columns)
iris.data.shape #(150, 4)
iris.target_names  # array(['setosa', 'versicolor', 'virginica'], dtype='<U10')
pd.unique(iris.target) #array([0, 1, 2])

"Let's check use all features"
X=iris.data

"####### Let's make 3 classifiers: #######"
Y=np.arange(100,550).reshape(150,3)
Y_train=np.arange(100,460).reshape(120,3)
Y_test=np.arange(100,190).reshape(30,3)
for ii in [0,1,2]:
    Y[:,ii]=(iris["target"]==ii).astype(np.int) # 

"split:"
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=101)

"let's use Logistic regression as the model:"
from sklearn.linear_model import LogisticRegression 
from sklearn import metrics
from sklearn.metrics import classification_report 
from sklearn.metrics import confusion_matrix

log_reg = LogisticRegression(random_state=101)

"for Setosa:"
log_reg.fit(X_train,Y_train[:,0])
y_proba0 = log_reg.predict_proba(X_test) 
y_pred0=log_reg.predict(X_test)
metrics.mean_squared_error(Y_test[:,0],y_pred0) # 0.0
r2_0=metrics.r2_score(Y_test[:,0],y_pred0)  #1.0
print(f"r^2 score for classifying Setosa is: {r2_0}")
target_names=["not Setosa","Setosa"]
print(classification_report(Y_test[:,0],y_pred0,target_names=target_names))
print("Setosa confusion matrix ")
conf0=confusion_matrix(Y_test[:,0],y_pred0)
keys=[['True Positive','False Negative'],['False Positive','True Negative']]
keys=pd.DataFrame(keys)
print(conf0)
print(keys)
print('___________________________________________________')
"for Versicolor:"
log_reg.fit(X_train,Y_train[:,1])
y_proba1 = log_reg.predict_proba(X_test) 
y_pred1=log_reg.predict(X_test)
metrics.mean_squared_error(Y_test[:,1],y_pred1) #0.26666666666666666
r2_1=metrics.r2_score(Y_test[:,1],y_pred1)  #-0.36363636363636354
print(f"r^2 score for classifying Vesicolor is: {r2_1}")
inderror=np.where(y_pred1!=Y_test[:,1])
errorrate=np.size(inderror)/len(y_pred1) # 3.3%
accuracy=1-errorrate
target_names1=["not Vesicolor","Vesicolor"]
print(classification_report(Y_test[:,1],y_pred1,target_names=target_names1))
print("Vesicolor confusion matrix ")
conf1=confusion_matrix(Y_test[:,1],y_pred1)
keys=[['True Positive','False Negative'],['False Positive','True Negative']]
keys=pd.DataFrame(keys)
print(conf1)
print(keys)
print('___________________________________________________')
"for Virginica:"
log_reg.fit(X_train,Y_train[:,2])
y_proba2 = log_reg.predict_proba(X_test) 
y_pred2=log_reg.predict(X_test)
metrics.mean_squared_error(Y_test[:,2],y_pred2) #0.0
r2_2=metrics.r2_score(Y_test[:,2],y_pred2)  #1.0
print(f"r^2 score for classifying Virginica is: {r2_2}")
target_names2=["not Virginica","Virginica"]
print(classification_report(Y_test[:,2],y_pred2,target_names=target_names2))
print("Virginica confusion matrix ")
conf1=confusion_matrix(Y_test[:,2],y_pred2)
keys=[['True Positive','False Negative'],['False Positive','True Negative']]
keys=pd.DataFrame(keys)
print(conf1)
print(keys)

import pandas as pd
df=pd.DataFrame(iris.data,range(0,150),['Sepal Length','Sepal Width','Petal Length','Petal Width'])
df.columns
dff=pd.concat([df,pd.DataFrame(iris.target,range(0,150),['Specie Label'])],1)
dff.head()
# Set style of scatterplot
import seaborn as sns
sns.set_context("notebook", font_scale=1.1)
sns.set_style("ticks")

# Create scatterplot of dataframe
sns.lmplot('Sepal Length','Sepal Width', data=dff, fit_reg=False,hue="Specie Label",scatter_kws={"marker": "D","s": 100}) # S marker size
sns.lmplot('Sepal Length', 'Petal Length', data=dff, fit_reg=False,hue="Specie Label",scatter_kws={"marker": "D","s": 100}) # S marker size
sns.lmplot('Sepal Length', 'Petal Width', data=dff, fit_reg=False,hue="Specie Label",scatter_kws={"marker": "D","s": 100}) # S marker size
sns.lmplot('Sepal Width', 'Petal Width', data=dff, fit_reg=False,hue="Specie Label",scatter_kws={"marker": "D","s": 100}) # S marker size
sns.lmplot('Sepal Width', 'Petal Length', data=dff, fit_reg=False,hue="Specie Label",scatter_kws={"marker": "D","s": 100}) # S marker size
sns.lmplot('Petal Width', 'Petal Length', data=dff, fit_reg=False,hue="Specie Label",scatter_kws={"marker": "D","s": 100}) # S marker size


# Set title
#plt.title('Iris Scatter')







