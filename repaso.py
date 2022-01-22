from mimetypes import init
import numpy as np


data = np.array([ [1.0, 2.0],
                  [3.0, 4.0],
                  [5.0, 6.0],
                  [7.0, 8.0]])


print(data)
print("Tipo de dato:" + str(type(data)))
print("Shape:" + str(data.size))
print("Size:" + str(data.size))
print("Ndim:" + str(data.ndim))
print("Nbytes:" + str(data.nbytes))
print("Dtype:" + str(data.dtype))

data = data.astype(np.int64)
print("Dtype modificado: " + str(data.dtype))