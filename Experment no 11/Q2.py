import numpy as np 
arr=np.array([1,2,3],dtype='int32')
print("Datatype:",arr.dtype)
arr=arr.astype('float64')
print("updated type:",arr.dtype)