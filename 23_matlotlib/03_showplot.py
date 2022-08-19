#####################################Line Plots########################################
# 1. Imports
import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:
# %matplotlib inline

# 2. Define data
x = np.arange(0, 4 * np.pi, 0.2)
y = np.sin(x)


# 3. Plot data including options
# Line Color, Line Width, Line Style, Line Opacity and Marker Options
# The color, width, and style of line in a Matplotlib plot can be specified. Line color, line width, 
# and line style are included as extra keyword arguments in the plt.plot() function call.

# plt.plot(<x-data>,<y-data>,
#             linewideth=<float or int>,
#             linestyle='<linestyle abbreviation>',
#             color='<color abbreviation>',
#             marker='<marker abbreviation>')

plt.plot(x, y,
    linewidth=0.5,  #unit:0.5 
    # linewidth=1,  #unit:0.5 
    # linestyle='--',  #dashed line
    # linestyle='-',  #solid  line
    linestyle='-.',  #dash-dot line
    # linestyle=':',  #dotted line
    color='b', #,b,c,g,k,m,r,w,y
    marker='o', #cicle
    # marker='*', #star
    markersize=10,
    markerfacecolor=(1, 0, 0, 0.1))


# 4. Add plot details
plt.title('Plot of sin(x) vs x from 0 to 4 pi')
plt.xlabel('x (0 to 4 pi)')
plt.ylabel('sin(x)')
plt.legend(['sin(x)']) # list containing one string
plt.xticks(
    np.arange(0, 4*np.pi + np.pi/2, np.pi/2),
    ['0','pi/2','pi','3pi/2','2pi','5pi/2','3pi','7pi/2','4pi'])
plt.grid(True)


# 5. Show the plot
plt.show()