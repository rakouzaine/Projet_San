import numpy as np
import matplotlib.pyplot as plt
def porte(t):
    y=(abs(t)<0.5)
    return np.float16(y)

# ---------------------------------------------------
Te = 0.01                   # période d’échantillonnage
t = np.arange(-5, 5, Te)    # axe temporel


# ---------------------------------------------------
# Deux portes standards
f = porte(t)
g = porte(t)
# FFT des deux signaux
F = np.fft.fft(f, n=2*len(f))  # zero-padding pour éviter aliasing
G = np.fft.fft(g, n=2*len(g))

# Produit dans le domaine fréquentiel
conv_fft = np.fft.ifft(F * G).real * Te

# Axe temps pour la convolution
t_conv = np.linspace(2*t[0], 2*t[-1], len(conv_fft))

plt.plot(t_conv, conv_fft)
plt.title("Convolution via transformée de Fourier")
plt.show()
