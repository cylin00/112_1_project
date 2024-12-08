import random
func = []
f = []
f.append(0)

x0 = 0
x1 = 500
delta = 1
n = 1
threshold = 0.000000001
s = 10
k = random.uniform(100., 400.)
#print(k)

for i in range(int((x1-x0)/delta)+1): #i from 0 to (x1-x0)/delta
    func.append(pow(x0+i*delta-k, 2))
    #print("f[", i, "] =", func[i])
func = []
#print(func)

while True:
    print('n=', n, 'x0=', x0, 'x1=', x1)
    c = x0
    for i in range(int((x1-x0)/delta)+1): #i from 0 to (x1-x0)/delta
        func.append(pow(x0+i*delta-k, 2))
        #print("f[", i, "] =", func[i])
    for i in range(int((x1-x0)/delta)):
        b1 = (func[i] < func[i-1]) & (i>0)
        b2 = (i<int((x1-x0)/delta)) & (func[i] < func[i+1])
        #print(i, b1, b2)
        if b1 & b2:
            c = x0 + i*delta 
    f.append(pow(c-k, 2))
    print(c, k)
    print(f)
    func = []
    x0 = c-delta
    x1 = c+delta
    delta /= s
    if n>1:
        if(abs(f[n]-f[n-1]) < threshold): #list index out of range
            print("f[", c, "] =", f[n], '; n =', n)
            print(f[n]-f[n-1])
            break
    n = n+1