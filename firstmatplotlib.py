#the father of all visualization packages in python is matplotlib
#inside the matplotlib subpackage there is pyplot subpackage
import matplotlib.pyplot as plt
import numpy as np
height=np.round(np.random.normal((500),1))
weight=np.round(np.random.normal((500),1))
#simple plot is line plot that just map the values of x axis to y axis and match the points and draw a line
plt.plot(height,weight)#x axis height and y axis weight
plt.show()
#scatter plot is also mapping but it just showing points of mapped values
plt.scatter(height,weight,color="r",marker="^")#x axis height and y axis weight
plt.show()
