#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.model_selection import train_test_split 

from matplotlib import interactive #this is to show the graphic automatically you need this if using IDLE
interactive(True)

# SECTION 1
print("SECTION 1")
rng = np.random.RandomState(1)
#x = 10 * np.random.rand(50)
x = 10 * rng.randn(50)

#y = 2 * x - 5 + np.random.randn(50)
y = 2 * x - 5 + rng.randn(50)
plt.scatter(x, y);
plt.show()

#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)

model.fit(x[:, np.newaxis], y)

xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])

plt.scatter(x, y)
plt.plot(xfit, yfit);
plt.show()

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.33)

model.fit(xtrain[:,np.newaxis],ytrain)
ypred=model.predict(xtest[:,np.newaxis])
print('Section 1 - coefficients:',model.coef_)

plt.scatter(xtrain, ytrain)
plt.scatter(xtest, ytest)
plt.scatter(xtest, ypred)
#input('press a key for section2')

# SECTION 2
#from sklearn import datasets, linear_model
#from sklearn.model_selection import train_test_split
print('SECTION 2')
height = np.round(np.random.normal(1.75,0.20,5000),2)
weight = np.round(np.random.normal(65.34,1.20,5000),2)
sample1=np.column_stack((height,weight))

htrain,htest,wtrain,wtest=train_test_split(height,weight,test_size=0.33)
len(htrain)
#3350
model1 = LinearRegression(fit_intercept=True)
model1.fit(htrain[:,np.newaxis],wtrain)

wpred=model1.predict(htest[:,np.newaxis])
print('Section 2 - coefficients:',model1.coef_)
plt.scatter(xtrain,ytrain)

