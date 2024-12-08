import random
k = random.uniform(100., 400.)
print("f = ( x -", k, ") ^ 2")

l = 0.3
threshold = 1e-6
des = 0

x = []
x.append(0)
n = 0
while(abs(pow(x[n]-k, 2)-des)>threshold):
    a = x[n] - l * (x[n] - k)
    x.append(a)
    n += 1

print("n =", n)
print("x[n] ", x[n])