import numpy as np
threshold = 1e-5
print("f(x, y) = ax^2 + by^2 + cx + dy + e")
a = input("a = ")
b = input("b = ")
c = input("c = ")
d = input("d = ")
e = input("e = ")

x0 = -200
y0 = -200
a1 = float(2*float(a)*x0 + float(c))
a2 = float(2*float(b)*x0 + float(d))
while(abs(a1)>threshold or abs(a2)>threshold):
    min = 1e30
    for lr in np.arange(0, 1, 0.01):
        x1 = x0 + lr*2*x0+1
        y1 = y0 + lr*2*y0+1
        #print(lr)
        if((float(a)*pow(x1, 2)+float(b)*pow(y1, 2)+float(c)*x1+float(d)*y1+float(e))<min):
            min = float(a)*pow(x1, 2)+float(b)*pow(y1, 2)+float(c)*x1+float(d)*y1+float(e)
            new_x = x1
            new_y = y1
    #print(l)
    x0 = new_x
    y0 = new_y
    a1 = float(2*float(a)*x0 + float(c))
    a2 = float(2*float(b)*x0 + float(d))
print(x0, y0)