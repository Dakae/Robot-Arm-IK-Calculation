import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Points A, B, C
A = np.array([10, 10, 10])
B = np.array([15, 15, 12])
C = np.array([16, 20, 4])

# Vectors AB and AC
AB = B - A
AC = C - A

# The normal vector to the plane is given by the cross product of AB and AC
normal_vector = np.cross(AB, AC)

# Equation of the plane: ax + by + cz = d
a, b, c = normal_vector
d = np.dot(normal_vector, A)

# Create a grid of x, y values to plot the plane
xx, yy = np.meshgrid(range(5, 25), range(5, 25))
zz = (d - a * xx - b * yy) / c

# Plotting the points A, B, C, the plane, and the lines AB and BC
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points with specified colors
ax.scatter(*A, color='r', s=100, marker='o', label='A')
ax.scatter(*B, color='g', s=100, marker='o', label='B')
ax.scatter(*C, color='b', s=100, marker='o', label='C')

# Plot the plane
ax.plot_surface(xx, yy, zz, color='yellow', alpha=0.5)

# Plot the lines AB and BC
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='black', label='Line AB')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], color='blue', label='Line BC')

# Labeling the points
ax.text(*A, 'A', fontsize=12, color='r')
ax.text(*B, 'B', fontsize=12, color='g')
ax.text(*C, 'C', fontsize=12, color='b')

# Setting labels for the axes
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Displaying the legend
ax.legend()

# Display the plot
plt.show()
