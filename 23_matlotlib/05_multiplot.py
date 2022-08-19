#####################################Line Plots########################################
import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:
# %matplotlib inline

x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)


fig, ax = plt.subplots()

ax.plot(x,y)
ax.plot(x,z)

ax.set_title('Two Trig Functions')
ax.legend(['sin','cos'])
ax.xaxis.set_label_text('Angle')
ax.yaxis.set_label_text('Sine and Cosine')

plt.show()