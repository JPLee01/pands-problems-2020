#John Paul Lee
#Problem Sheet for Week 8 of Programming and Scripting

#Import matplotlib abd numpy
import matplotlib.pyplot as plt
import numpy as np

#set the range along the x axis in intervals of 0.01 to allow for smooth graph
l = np.arange (0.0, 4.0, 0.01)

n = float(input("Please enter a number between 0-4: "))
#Define f, g and h (have user input a number)
f = n
g = f**2
h = f**3

#Even though the below is the definitions of f,g and h a figure is required for (f)to generte a plot
#f = x
#g = x**2
#h = x**3

#Plot the points and label them according to thier functions
plt.plot(f, 'r.', label = "f(x)=x")
plt.plot(g, 'g.', label = "g(x)=x2")
plt.plot(h, 'b.', label = "h(x)=x3")

#Plot a dashed line connecting the points (if wanted to) along x and y axis
#plt.plot([f, g, h], [f, g, h], marker='o', color='c')

#Insert a name of the X axis
plt.xlabel("X Axis")

#Insert a name of the Y axis
plt.ylabel("Y Axis")

#Insert a Title
plt.title("Visual Representation of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.")

#Insert Legend
plt.legend()

#Grid the graph
plt.grid()

#Display the plot
plt.show()


#References:
# Real Python "Python Plotting With Matplotlib (Guide)" https://realpython.com/python-matplotlib-guide/
# https://realpython.com/python-matplotlib-guide/
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# https://python-graph-gallery.com/matplotlib/



