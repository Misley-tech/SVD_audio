import matplotlib.pyplot as plt
import numpy as np
import time

from PIL import Image

img = Image.open('C:/Users/Asus/Desktop/programitas/SVD/prueba.png')
imggray = img.convert('LA')

imgmat = np.array(list(imggray.getdata(band=0)), float)
imgmat.shape = (imggray.size[1], imggray.size[0])
imgmat = np.matrix(imgmat)

U, sigma, V = np.linalg.svd(imgmat)

# cantidad de términos de la serie considerada
r = 50

for i in range(1, r):
    plt.figure(figsize=(9,6))   
    reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
    plt.imshow(reconstimg, cmap='gray')
    plt.title(f'Imagen reconstruida con $r = {i}$ de ${len(sigma)}$, espacio ocupado: {round((i*100)/len(sigma),2)} $ \% $',fontsize=15)
    plt.show()

r=1
suma=np.zeros(np.shape(A))
for i in range(r):
    suma=singular_values[i]*(np.transpose([U[i]])@([V_t[i]]))
print(np.real(suma[0]))
sf.write('HolaSVD_reconstruccion.wav',np.real(suma[0]),fs)