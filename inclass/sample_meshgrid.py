import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
from matplotlib import interactive #this is to show the graphic automatically you need this if using IDLE
import numpy as np

interactive(True) #setting this will show the graph as it is plotted

xvalues, yvalues = np.array([0, 1, 2, 3, 4]),np.array([0, 1, 2, 3, 4])
h=0.01
xx, yy = np.meshgrid(xvalues, yvalues)
plt.plot(xx, yy,marker='.', color='k', linestyle='none')
#[<matplotlib.lines.Line2D object at 0x000000000A4C9A90>, <matplotlib.lines.Line2D object at 0x000000000A4C9C18>, <matplotlib.lines.Line2D object at 0x000000000A4C9D30>, <matplotlib.lines.Line2D object at 0x000000000A4C9E80>, <matplotlib.lines.Line2D object at 0x000000000A4C9FD0>]
plt.show()
