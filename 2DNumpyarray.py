import numpy as np
#numpy type is ndarray that means N-dimensional Array.
#Now lets make a 2d array
family=np.array([[1,2,3,4,5,6,7,8],['A','B','C','D','E','F','G','H']])
print(family)
# shape method tells us about the structure of data structure
print(family.shape)
# The numpy 2D arrya can only be of one type
#but lets work on prevous array
#Subsetting in different ways lets play
print(family[0])
print(family[:])
print(family[1])
#it prints as a matrix
print(family[:,1:3])
print(family[1,0])
print(family[:,2])
