import numpy as np
quad = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])

print("Please enter 4 coordinates in the following format:")
print("X1 Y1 Z1")
print("X2 Y2 Z2")
print("X3 Y3 Z3")
print("X4 Y4 Z4")

for i in range(4):
    quad[i] = np.array(list(map(float, input().split())))

print("Given coordinates:")
print(quad)
print()

print("Center of mass coordinates:")
print(*np.average(quad, axis=0))