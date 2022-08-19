#####################################Line Plots########################################
# Matplotlib plots can be saved as image files using the plt.savefig() function.
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:
# %matplotlib inline

x = [0, 2, 4, 6]
y = [1, 3, 4, 8]


plt.plot(x,y)


plt.xlabel('x values')
plt.ylabel('y values')
plt.title('plotted x and y values')
plt.legend(['line 1'])


# save the figure
plt.savefig('04_saveplot.png', dpi=300, bbox_inches='tight')


plt.show()