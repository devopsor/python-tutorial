#####################################Box Plots########################################
import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:
# %matplotlib inline

# generate some random data
data1 = np.random.normal(0, 6, 100)
data2 = np.random.normal(0, 7, 100)
data3 = np.random.normal(0, 8, 100)
data4 = np.random.normal(0, 9, 100)
data = list([data1, data2, data3, data4])


fig, ax = plt.subplots()


# build a box plot
ax.boxplot(data)


# title and axis labels
ax.set_title('box plot')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
xticklabels=['category 1', 'category 2', 'category 3', 'category 4']
ax.set_xticklabels(xticklabels)


# add horizontal grid lines
ax.yaxis.grid(True)


# show the plot
plt.show()