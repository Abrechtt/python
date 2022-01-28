import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

frecuencia_muestreo, muestra = wavfile.read("trompeta.wav")
print("frecuencia muestreo: " + str(frecuencia_muestreo))
print("tipo de dato arreglo de muestra: " + str(type(muestra)))
print("Dtype: " + str(muestra.dtype))
print("shape: " + str(muestra.shape))

duracion = muestra.shape[0] / frecuencia_muestreo
print("time: " + str(duracion))

print("FORMATO")
print("frecuencia muestreo: " + str(frecuencia_muestreo))
profundidad_bits = 32
if (muestra.dtype == np.int16):
    profundidad_bits = 16
elif (muestra.dtype == np.uint8):
    profundidad_bits = 8
print("profundidad: " + str(profundidad_bits))

canales = 1
if (len(muestra.shape) > 1):
    canales = muestra.shape[1]
print("cantidad de canales: " + str(canales))

tiempos = np.linspace()

plt.figure()
if canales == 1:
    plt.plot(tiempos, muestra, label = "Canal mono")   
else:
    plt.plot(tiempos, muestra[:, 0], label = "Canal izquierdo")
    plt.plot(tiempos, muestra[:, 1], label = "Canal derecho")
plt.legend()
plt.xlabel("timepo")
plt.ylabel("amplitud")
plt.show()