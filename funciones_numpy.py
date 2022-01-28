import numpy as np

#lista de python
datos = np.array([1,2,3])

#lista muldidimensional
datos = np.array([[1,2], [3,4]])

#ceros
datos = np.zeros((5,3))

#unos
datos = np.ones((4,3), dtype=np.int64)

#constante arbitrarias
datos = np.ones((4,3)) * 3.5
datos = np.full((4,3), 3.5)
datos = np.empty((5,4))
datos.fill(7,4)

#seceuncia incremental / arange excluye stop
datos = np.arange(15)
#start, stop, step
datos = np.arange(2,15,4)

#secuencia incremental / base al numero de elementos
datos = np.linspace(0,10,20)


print(datos)