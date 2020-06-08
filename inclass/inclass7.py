'''

-----------------------------------------HW---------------------------------------------------
decision tree characteristics-- to worksheet:
    nonparametric
    supervised?
    binary tree(has to have at most 2 part in each dallarında(tr))
    veriler neler olabilir
    multiclassifier?


'''




"""
random.seed()-

"""



import random


print(random.randrange(10))
print(random.sample([1,2,3,4,5,6,7],5))
print(random.sample(range(30,70),5))



random.seed(10)
print(random.randrange(10,20))
random.seed(10)
print(random.sample(range(30,70),3))
random.seed(10)
print(random.randrange(10,20))




'''
maximum tree depth:
en fazla 10 kola ulaşınca daha fazla gitme
minimum node records:
son aşamada belli sayının altında eleman varsa daha küçülme(mesela 10 eleman)


eğer 3 sıra decision tree varsa onun derinliğine 2 deriz.



CART:
    greedy approach to divide by recursive binary splitting
    when it is done there will be cost function

Construction Tree:
...

Gini index:
    name of cost func used to evaluate splits in the dataset
    gives idea of how good split
    perfect splitting score is: 0 gini score -if homogenious
    worst case: 50/50--- 0.5 gini score -if heterous
    
impurity of nodes: (check what it is mean
    minimize impurity in each node(Decision tree)

Entropy:
    amount of information disorder
    if equally divided entropy is 1
    if completely homogenious entropy is 0
    entropy function is in the slides
    
    
informaiton gain:
    how much extra information is gained by splitting
    calculated by using entropy 

Decisiom tree classifier:
    form skllearn.tree import DeicsionTreeClassifier
        .... rest of the code on slides 
        classifierx.fit(input,output)- creates decision tree by itself (check how it works)
        classifierx.predict(input)- predict itself outcome with defined parameters in classifierx(you will do it check slides)
        aşağıda kodlar yazıldı....
 
'''
# bazen data alırken (r'/Users/metehaangelgi/...iris.csv')
# yazılmasının sebebi içindek ikaçış karakterlerinin hepsinin string olduğunu göstermek

import numpy as np
import os
print(os.getcwd())
print(np.random)
print(np.arange(100))

a1=np.arange(100).reshape(20,5)
print(a1)


a1=a1.reshape(10,10)
print(a1)

import pandas as pd


datasetIris=pd.read_csv("iris.csv")

#print(datasetIris.read())
print(datasetIris.head(10))
print(datasetIris.describe())




#-----------------------

from sklearn.datasets import load_iris
#from sklearn.model_selection import cross_validate

iris=load_iris()
X=iris.data
Y=iris.target
print("------------------------------------------------------")
print(Y)
print(iris.target_names)
print(type(iris))



from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=0)

estimator=DecisionTreeClassifier(max_leaf_nodes=3,random_state=0)
estimator.fit(X_train,Y_train)
my_tree=estimator.tree_
print("*************************")
print(my_tree)
print(X_train)
print(Y_train)
print(X_test)
print(Y_test)
print(type(estimator))
print(estimator.fit(X_train,Y_train))
estimator.tree_



print(estimator.predict(X_train))
print()
Y_pred=estimator.predict(X_test)
print(estimator.predict(X_test))# is almost same with-- print(Y_test)--- because this is just predict of outcome
print()
print(Y_test)#actual outcome

'''
np.complete--- check it 
'''



'''
confusion matrix:
    true-false   
    positive-negative
    helps your predict is true enough with outcome 
    
binary classification:
    entry i,j-- actually in group i but predicted as group j
    positive and negative--refers to classifiers prediction
    true or false--- whather prediction corresponds to the eternal judgement 
    a-true-positive
    b-false-positive
    c-true-negative
    d-false-negative
    rows prediction
    coloumns are actual 
    
        YES     NO
    YES 61(a) 16(b)
    NO  19(d) 64(c)
    
    -19 (aka type 1 error )--you are ill but ı am not --potansiyel kar engelleniyo--zarar yok 
    -16(aka type 2 error )--you are healty but ı am ill---gerçek zarar verilir 
    --bu hataların tanımlarını bil--
    
terms related with confusion matrix:(check photo)
    Accuracy:overall, how often is the classifier is correct ---(61+64)/160
    Misclassification rate: overall, how often wrong----(19+16)/160---Error Rate(==1-Accuracy)
    True Positive Rate:when yes, how often yes?-----(61/80)-----(Sensitivity or Recall)
    False positive Rate: when actually no, predict yes------16/80
    Specificity:when actually no,how often predict no-----64/80(1-False Positive Rate)
    Precision:predicts yes,how often true?--------61/(61+16)
    Prevalence:how often yes condition actually occur in our sample?-------80/160
    positive predict Value:probability that subjects with a positive screening test truly have disease
    Negative Predict Value   prob.      t.   s.      w.   a negative s.        test  truly have not disease
    
    #######multi class-matrices
    rows-FN(except TP)
    coloumn-FP(except TP)
    all things excluding target classes rows and coloumns(+ gibi yeri alma)-TN
    --bunun formülleri resimdeki ile aynı fakat FN,FP,TN için buraya bak
    
    ROC curve- sınav sonrası için 
    
    
            
'''

from sklearn.metrics import confusion_matrix
print(confusion_matrix(Y_test,Y_pred))
'''


-----------------------------------SINAV KONULARI-----------------------------
1 affaintyi
1 kod 
1 confusion_matrix()
1 decision tree

'''



