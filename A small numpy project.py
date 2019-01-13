import numpy as np
#First get the sample data from the numpy
height=np.round(np.random.normal(1.75,0.20,5000),2)#this is a distribution of 5000 samples values for the first column
weight=np.round(np.random.normal(60.32,15,5000),2)  # in both height and weight first value is distribution mean second is standard deviation
np_city=np.column_stack((height,weight))#now we have an array with two columns
print(np_city)
hmean=np.mean(np_city[:,0])#first height column mean
print(hmean)
wmean=np.mean(np_city[:,1])#first weight column mean
print(wmean)
hmedian=np.median(np_city[:,0])# first column median
print(hmedian)
wmedian=np.median(np_city[:,1])# second column median
print(wmedian)
#findng correlation cofficient of both columns
cor=np.corrcoef(np_city[:,0],np_city[:,0])
print(cor)
hstn=np.std(np_city[:,0])# second column Standard deviation
print(hstn)
wstn=np.std(np_city[:,1])# second column Standard Deviation
print(wstn)
