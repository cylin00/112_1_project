import csv
import numpy as np

path = r"/Users/chinying/Desktop/ee/ee5/re/0907/data2.csv"
original_data = []
predict_data = []
parameter = []
n1, n2, n3, n4 = 50, 199, 200, 251
mse = 1e30
best_L = 0

with open(path, 'r') as data:
    #trans data.csv into an array
    data_content = csv.reader(data, delimiter=',')
    next(data_content)

    #training data : 0-199
    #test data : 200-251
    for row in data_content:
        original_data.append(row[1])
        predict_data.append(row[1])
    for i in range(len(predict_data)):
        predict_data[i] = 0 #=? find ak
    
    #find ak
    
    for L in range(1, 50): #1 to 200
        mat1 = [[0 for x in range(L)] for y in range(L)]
        for i in range(L): #0 to L-1
            for j in range(L):
                for n in range(n1, n2+1): #n1 to n2
                    mat1[i][j] += float(original_data[n-i-1])*float(original_data[n-j-1])
        mat2 = np.linalg.inv(mat1)
        mat3 = []
        for k in range(L):
            mat3.append(0)
            for n in range(n1, n2+1):
                    mat3[k] += float(original_data[n])*float(original_data[n-k-1])
        parameter = np.matmul(mat2, mat3)
        #print(parameter)
        #print(L)
        #calculate mse
        mse_L = 0
        for n in range(n3, n4+1): #n3 to n4
            pred = 0 
            for k in range(L):
                pred += parameter[k]*float(original_data[n-k])
            print(f"prediction: {pred}, practical: {original_data[n]}")
            mse_L += np.square(float(original_data[n]) - pred)
        
        if (mse_L < mse) & (L != 1):
            mse = mse_L
            best_L = L
        print("mse_L =", mse_L)
        print("mse =", mse)
        print("L =", L)
        print("best_L =", best_L)


