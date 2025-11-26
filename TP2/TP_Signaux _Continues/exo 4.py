import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------
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


h = np.convolve(f, g, mode='full') * Te

# Axe temporel correspondant
t_conv = np.arange(2 * len(t) - 1) * Te + 2 * t[0]

# 🔹 Affichage
plt.subplot(3, 1, 1)
plt.plot(t, f, label='f(t) = Π(t)')
plt.subplot(3, 1, 1)
plt.title("Produit de convolution de deux portes standards")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.plot(t, g, label='g(t) = Π(t)')
plt.subplot(3, 1, 1)
plt.title("Produit de convolution de deux portes standards")

plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t_conv, h, 'r', label='(f * g)(t)')
plt.title("Produit de convolution de deux portes standards")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()



import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# Exercice 1
# --------------------------
def conv_ex1(t):
    # Expression analytique
    h = np.zeros_like(t)
    # 0 <= t <= 1 : 2t
    mask = (t >= 0) & (t <= 1)
    h[mask] = 2 * t[mask]
    # 1 < t <= 2 : 2
    mask = (t > 1) & (t <= 2)
    h[mask] = 2.0
    # 2 < t <= 3 : 2(3-t)
    mask = (t > 2) & (t <= 3)
    h[mask] = 2 * (3 - t[mask])
    return h

# --------------------------
# Exercice 2
# --------------------------
def conv_ex2(t):
    h = np.zeros_like(t)
    # regions
    # -1 <= t <= 1: (t^2)/4 + t/2 + 1/4
    mask = (t >= -1) & (t <= 1)
    h[mask] = (t[mask]**2) / 4.0 + t[mask] / 2.0 + 1/4.0
    # 1 < t <= 3 : h = 1
    mask = (t > 1) & (t <= 3)
    h[mask] = 1.0
    # 3 < t <= 5 : -t^2/4 + 3/2 t - 5/4
    mask = (t > 3) & (t <= 5)
    h[mask] = -0.25 * t[mask]**2 + 1.5 * t[mask] - 1.25
    return h

# --------------------------
# Exercice 3 (analytique)
# --------------------------
def conv_ex3(t, a=1.0, b=2.0):
    C = np.sqrt(2 * np.pi / (a + b))
    return C * np.exp(- (a * b) / (2 * (a + b)) * t**2)

# --------------------------
# Domaine de tracé
# --------------------------
t1 = np.linspace(-1, 4, 800)   # pour ex1 (support [0,3]) - on affiche un peu autour
t2 = np.linspace(-2, 6, 800)   # pour ex2 (support [-1,5])
t3 = np.linspace(-6, 6, 800)   # pour ex3 (gaussienne)
# Tracés
plt.figure(figsize=(12, 8))

plt.subplot(3,1,1)
plt.plot(t1, conv_ex1(t1), label='h = f * g (Exercice 1)')
plt.title('Exercice 1 : convolution de f(t)=2_{[0,2]} et g(t)=1_{[0,1]}')
plt.xlabel('t'); plt.ylabel('h(t)')
plt.xlim(-1,4)
plt.grid(True); plt.legend()

plt.subplot(3,1,2)
plt.plot(t2, conv_ex2(t2), label='h = f * g (Exercice 2)')
plt.title('Exercice 2 : convolution (fonctions données)')
plt.xlabel('t'); plt.ylabel('h(t)')
plt.xlim(-2,6)
plt.grid(True); plt.legend()

plt.subplot(3,1,3)
a = 1.0; b = 2.0
plt.plot(t3, conv_ex3(t3,a,b), label=f'Convolution gaussiennes a={a}, b={b}')
plt.title('Exercice 3 : convolution de deux gaussiennes (formule analytique)')
plt.xlabel('t'); plt.ylabel('h(t)')
plt.xlim(-6,6)
plt.grid(True); plt.legend()

plt.tight_layout()
plt.show()
