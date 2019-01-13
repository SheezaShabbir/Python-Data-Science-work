import numpy
print(numpy.array([1,2,3,4,5,6]))
import numpy as np
print(np.array([1,2,3,4,5,6]))
from numpy import array
print(array([1,2,3,4,5,6,7]))
# Numpy is a numeric python.
#it is alternative to the python lists
#it performs calculation on large dataset over entire arrays
#it is also super fast.
#Comparing with others it is really tidy to perform array calculation without numpy
# watch below how it make calculation so easy for you have a look ;)
np_height=array([1.2,3.4,2.3,4.5])
np_weight=array([1.2,3.4,2.3,4.5])
answer=np_height/np_weight**2
print(answer)
# numpy take only single type of arrray
#if you try to give it mix with int, boolean and string ,It will consider all others strings as well.
#others magics of numpy
# lets if you want to get subset of answer it will like that given below
print(answer[2])
print(answer>0.1)
print(answer[answer>0.1])
#one more thing is that it performs elementwise calculations
import numpy as np
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = x + y*2
print(z)
