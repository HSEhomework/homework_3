import numpy
import numpy as np

print("Please enter 4 coordinates in the following format:")
print("X1 Y1 Z1")
print("X2 Y2 Z2")
print("X3 Y3 Z3")
print("X4 Y4 Z4")

A = np.array(list(map(float, input().split())))
B = np.array(list(map(float, input().split())))
C = np.array(list(map(float, input().split())))
D = np.array(list(map(float, input().split())))

print("A coordinates: ", *A)
print("B coordinates: ", *B)
print("C coordinates: ", *C)
print("D coordinates: ", *D)

a = np.zeros((4, 3))
b = np.zeros(4)

a[0][0] = C[1] - A[1]
a[0][1] = A[0] - C[0]
a[0][2] = 0

a[1][0] = 0
a[1][1] = C[2] - A[2]
a[1][2] = A[1] - C[1]

a[2][0] = D[1] - B[1]
a[2][1] = B[0] - D[0]
a[2][2] = 0

a[3][0] = 0
a[3][1] = D[2] - B[2]
a[3][2] = B[1] - D[1]

b[0] = A[0] * (C[1] - A[1]) - A[1] * (C[0] - A[0])
b[1] = A[1] * (C[2] - A[2]) - A[2] * (C[1] - A[1])
b[2] = B[0] * (D[1] - B[1]) - B[1] * (D[0] - B[0])
b[3] = B[1] * (D[2] - B[2]) - B[2] * (D[1] - B[1])

print("a*E=b, where E - intersection point of diagonals")
print("a:")
print(a)
print("b: ", b, end='\n\n')
isCorrect = False
for k in range(4):
    c = []
    d = []
    for i in range(4):
        if i != k:
            c.append(a[i])
            d.append(b[i])
    c = numpy.array(c)
    d = numpy.array(d)

    try:
        E = np.linalg.solve(c, d)

        if np.linalg.norm(np.dot(a[k], E) - b[k]) < 1e-10:
            isCorrect = True
            F = C + (A - E)
            print("E coordinates: ", *E)
            print("F coordinates: ", *F)
            print("Center of mass coordinates: ", *((D + B + F) / 3))
            break

    except np.linalg.LinAlgError as err:
        pass

if not isCorrect:
    print("Incorrect input, there is no intersection point of diagonals")