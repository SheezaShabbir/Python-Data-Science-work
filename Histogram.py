#The histogram is a type of visualization that's particularly useful to explore your data sets.
#It can help you to get an idea about the distribution of your variables.
import matplotlib.pyplot as plt
import numpy as np
values=np.random.normal(500)
help(plt.hist)
plt.hist(values,bins=10)
plt.show()
plt.clf()#the method is used to clear plot
#by default bins made by python are 10 if you not mention the bins
