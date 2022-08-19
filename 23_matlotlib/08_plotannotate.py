import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:
# %matplotlib inline

x = np.arange(-5, 5, 0.01)
y = x**2


fig, ax = plt.subplots()


# Plot a line
ax.plot(x, y)


# first annotation relative to the data
ax.annotate('function minium \n relative to data',
            xy=(0, 0),
            xycoords='data',
            xytext=(2, 3),
            arrowprops=
                dict(facecolor='black', shrink=0.05),
                horizontalalignment='left',
                verticalalignment='top')


# second annotation relative to the axis limits
bbox_props = dict(boxstyle="round,pad=0.5", fc="w", ec="k", lw=2)


ax.annotate('half of range \n relative to axis limits',
            xy=(0, 0.5),
            xycoords='axes fraction',
            xytext=(0.2, 0.5),
            bbox=bbox_props,
            arrowprops=
                dict(facecolor='black', shrink=0.05),
                horizontalalignment='left',
                verticalalignment='center')


# third annotation relative to the figure window
bbox_props = dict(boxstyle="larrow,pad=0.5", fc="w", ec="k", lw=2)


ax.annotate('outside the plot \n relative to figure window',
            xy=(20, 75),
            xycoords='figure pixels',
            horizontalalignment='left',
            verticalalignment='top',
            bbox=bbox_props)


ax.set_xlim(-5,5)
ax.set_ylim(-1,10)
ax.set_title('Parabolic Function with Text Notation')


plt.show()