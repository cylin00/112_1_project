import random
e = (-1+pow(5, 0.5))/2
k = random.uniform(100., 900.)
print(k)

x0 = 1
x1 = 1000
n = 1
x2 = x0 + (x1-x0)/(1+e)
threshold = 0.000001


while True:
    
    x3 = x0 + (x2-x0)/(1+e)

    print('n =', n)
    print(x0, x1, x2, x3)

    if(pow(x3-k, 2) > pow(x2-k, 2)):
        x0 = x1
        x1 = x3
        
    elif(pow(x3-k, 2) < pow(x2-k, 2)):
        x1 = x2
        x2 = x3

    n +=1 

    if(abs(x0-x1) < threshold):
        break
