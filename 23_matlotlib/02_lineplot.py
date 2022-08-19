#####################################Line Plots########################################
# Line plots can be created in Python with Matplotlib's pyplot library. 
# To build a line plot, first import Matplotlib. It is a standard convention to import Matplotlib's pyplot library as plt. 
# The plt alias will be familiar to other Python programmers

import matplotlib.pyplot as plt
import numpy as np
# if using a Jupyter notebook, include:
# %matplotlib inline
x = np.arange(0, 4 * np.pi, 0.1)
print(x)
y = np.cos(x)
print(y)
plt.plot(x, y)
plt.show()