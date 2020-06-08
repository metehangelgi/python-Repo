import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

iris = datasets.load_iris()
N=15
clf = neighbors.KNeighborsClassifier(N)
clf

X2 = iris.data[:-4, :2]
y2=iris.target[:-4]

# use a random sampling see the target values
# this code is just for basic reference
clf.fit(X2,y2)
clf.predict(X2[-4:,:])
# array([1, 2, 2, 2])
y2pred=clf.predict(X2[-4:,:])
y2[-4:]
# array([2, 2, 2, 2])
