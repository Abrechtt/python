import numpy as np

data = np.arange(0,11)
indice = 6
print(data)

print("indice 0: "  +  str(data[0]) )
print("indice 10: "  +  str(data[10]) )

#index out of bounds
#print("indice 16: "  +  str(data[16]) )

#Si usamos variables en los indices
#tienen que ser int
print("indice 'indice': " + str(data[indice]))

print("Indice -1; " + str(data[-1]))
print("Indice -7: "+ str(data[-7]))

#Out of bounds
#print("Indice -16: "+ str(data[-16]))

#rangos [m:n]
#m se incluye 
#n se excluye
#Rango siempre regresa un arreglo
print("Indice [1:4]: " + str(data[1:4]))
#Regresa un arreglo vacio
print("Indice [1:1]: " + str(data[1:1]))

print("Indice [1:2]: " + str(data[1:2]))
#Si no le doy rangos validos, me regresa vacío
print("Indice [4:1]: " + str(data[4:1]))
#No existe el indice 11, pero no marca error
#porque nunca intenta acceder a el
print("Indice [1:11]: " + str(data[1:11]))
#Si se sale de los límites, no marca error,
#solo te regresa hasta donde puede
print("Indice [1:15]: " + str(data[1:15]))

print("Indice [2:-3]: " + str(data[2:-3]))

print("Indice [-9:-3]: " + str(data[-9:-3]))

#El 3er parametro del rango es el "step"
print("Indice [1:-1:2]: " + str(data[1:-1:2]))

#Los parametros de los rangos son opcionales
#Si se omite el primero (m) lo toma como el primer elemento
print("Indice [:5] " + str(data[:5]))
#Si se omite el segundo (n) lo  toma como el último elemento
print("Indice [2:] " + str(data[4:]))
print("Indice [-6:] " + str(data[-6:]))
#Si se omiten ambos (m y n) lo toma desde el primero hasta el último
#Solo contemple el step
print("Indice [::3] " + str(data[::3]))
print("Indice [::-1] " + str(data[::-1]))

elemento = data[5]
elemento = 7
data[5] = 7
print("Elemento: " + str(elemento))
print("data: " + str(data))

#Si se modifica un segmento obtenido por rango de un ndarray
#También se ve modificado el ndarray original
segmento = data[1:10:2]
print("segmento: " + str(segmento))
segmento[0] = 24
print("segmento 2: " + str(segmento))
print("data: " + str(data))


#si se modifica el ndarray original
#también se ve modificando el segmento
data[5] = 48
print("data: " + str(data))
print("segmento 3: " + str(segmento))