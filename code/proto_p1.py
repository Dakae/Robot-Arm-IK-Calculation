import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Points A, B, C
A = np.array([10, 10, 10])
B = np.array([15, 15, 12])
C = np.array([16, 20, 4])

# Defining the new point B0 based on the given instructions
B0 = np.array([15, 15, 2])

# Vectors AB and AB0
AB = B - A
AB0 = B0 - A

# The normal vector to the plane P1 is given by the cross product of AB and AB0
normal_vector = np.cross(AB, AB0)

# Equation of the plane P1: ax + by + cz = d
a, b, c = normal_vector
d = np.dot(normal_vector, A)

# Re-calculating the grid with consideration that the plane is vertical.
xx, zz = np.meshgrid(range(5, 25), range(-5, 15))
yy = (d - a * xx - c * zz) / b

# To project point C onto the plane P1, we calculate the projection vector.

# The normal vector to the plane P1
normal_vector = np.array([a, b, c])

# Vector BC
BC = C - B

# Projection of BC onto the normal vector
projection_length = np.dot(BC, normal_vector) / np.linalg.norm(normal_vector)
projection_vector = projection_length * normal_vector / np.linalg.norm(normal_vector)

# The projection of C onto the plane P1 (i.e., point Cp1)
Cp1 = C - projection_vector

# Calculate the new point that is 4 units away from B0, along the direction of the normal vector of P1
# Normalize the normal vector
normalized_normal = normal_vector / np.linalg.norm(normal_vector)

# Calculate the new point (let's call it D) that is 4 units away from B0 along the normal vector
D = B0 + 4 * normalized_normal

# Plotting the points, the plane P1, and the new point D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original points as dots
ax.scatter(*A, color='r', s=100, marker='o', label='A')
ax.scatter(*B, color='g', s=100, marker='o', label='B')
ax.scatter(*B0, color='purple', s=100, marker='o', label='B0')
ax.scatter(*C, color='b', s=100, marker='o', label='C')
ax.scatter(*Cp1, color='orange', s=100, marker='o', label='Cp1')
ax.scatter(*D, color='pink', s=100, marker='o', label='D')  # New point D

# Plot the plane P1
ax.plot_surface(xx, yy, zz, color='yellow', alpha=0.5)

# Plotting lines connecting A-B, B-C, B-B0, B-Cp1, and B0-D
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='black', label='Line AB')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], color='blue', label='Line BC')
ax.plot([B[0], B0[0]], [B[1], B0[1]], [B[2], B0[2]], color='green', label='Line BB0')
ax.plot([B[0], Cp1[0]], [B[1], Cp1[1]], [B[2], Cp1[2]], color='orange', linestyle='--', label='Line BCp1')
ax.plot([B0[0], D[0]], [B0[1], D[1]], [B0[2], D[2]], color='pink', linestyle='--', label='Line B0D')

# Labeling the points
ax.text(*A, 'A', fontsize=12, color='r')
ax.text(*B, 'B', fontsize=12, color='g')
ax.text(*B0, 'B0', fontsize=12, color='purple')
ax.text(*C, 'C', fontsize=12, color='b')
ax.text(*Cp1, 'Cp1', fontsize=12, color='orange')
ax.text(*D, 'D', fontsize=12, color='pink')

# Setting labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Displaying the legend
ax.legend()

# Display the plot
plt.show()
