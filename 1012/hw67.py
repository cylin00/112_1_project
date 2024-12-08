import csv
import numpy as np
import random
import matplotlib.pyplot as plt

k = input("Input the number of points >> ")
A = [[0 for x in range(2)] for y in range(int(k))]

xsum = 0
ysum = 0
for i in range(int(k)): #0 to k-1
    A[i][0] = random.randint(0, 101)
    A[i][1] = random.randint(0, 101)
    xsum += A[i][0]
    ysum += A[i][1]
xmean = float(xsum) / float(k)
ymean = float(ysum) / float(k)
#print(A, xmean, ymean)
for i in range(int(k)):
    A[i][0] -= xmean
    A[i][1] -= ymean

corr = 0
for i in range(int(k)):
    corr += (A[i][0]-xmean)*(A[i][1]-ymean)
X = 0
Y = 0
for i in range(int(k)):
    X += pow(A[i][0]-xmean, 2)
    Y += pow(A[i][1]-ymean, 2)
corr = float(corr)/float(pow(X*Y, 0.5))
print("correlation =", corr)

U, S, Vh = np.linalg.svd(A, full_matrices=True)
V = Vh.transpose()
x1 = xmean + -50*V[0][0]
y1 = ymean + -50*V[1][0]
x2 = xmean + 50*V[0][0]
y2 = ymean + 50*V[1][0]
xval = [x1, x2]
yval = [y1, y2]
#print(V)
for i in range(int(k)):
    plt.plot(A[i][0]+xmean, A[i][1]+ymean, "-o")
plt.plot(xval, yval)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()