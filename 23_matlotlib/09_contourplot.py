import matplotlib.pyplot as plt
import numpy as np
# if using a Jupyter notebook, include:
# %matplotlib inline

x = np.arange(-3.0, 3.0, 0.1)
y = np.arange(-3.0, 3.0, 0.1)

X, Y = np.meshgrid(x, y)

Z = np.sin(X)*np.cos(Y)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))

mycmap1 = plt.get_cmap('gist_earth')
ax1.set_aspect('equal')
ax1.set_title('Colormap: gist_earth')
cf1 = ax1.contourf(X,Y,Z, cmap=mycmap1)

fig.colorbar(cf1, ax=ax1)

mycmap2 = plt.get_cmap('gnuplot2')
ax2.set_aspect('equal')
ax2.set_title('Colormap: gnuplot2')
cf2 = ax2.contourf(X,Y,Z, cmap=mycmap2)

fig.colorbar(cf2, ax=ax2)

plt.show()