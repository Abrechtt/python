import numpy as np

datos = np.array([[1,2], [3,4]])
#print(datos)

#unos
datos = np.ones((4,3), dtype=np.int64)
#print(datos)
#print(datos.dtype)

#constante arbitrarias
datos = np.ones((4,3)) * 3.5

print(datos)