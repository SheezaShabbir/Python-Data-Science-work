#The histogram is a type of visualization that's particularly useful to explore your data sets.
#It can help you to get an idea about the distribution of your variables.
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,4,6,8,10,12,14,16,18,20]
#plt.plot(x,y)
plt.fill_between(x,y,0,color="green")#here 0 value says that we want to filling start from the 0
plt.xlabel("values of X")
plt.ylabel("values of Y")
plt.title("The first graph of Customization")
plt.yticks([2,4,6,8,10],['0','2B','2C','2D','2E'])
plt.show()
plt.clf()#the method is used to clear plot
help(plt.scatter)
#by default bins made by python are 10 if you not mention the bins
col=["green","red","blue","yellow"]
plt.scatter(x = x, y = y,c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71,1)#It add the values
plt.text(5700, 80,2)#the third argument is for the position

# Add grid() call
plt.grid(True)#it draws gridlines in the graph

# Show the plot
plt.show()
