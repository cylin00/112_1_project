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