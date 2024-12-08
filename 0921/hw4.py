import csv
import numpy as np

path = r"/Users/chinying/Desktop/ee/ee5/re/0907/data2.csv"
original_data = []
predict_data = []
parameter = []
n1, n2, n3, n4 = 50, 199, 200, 251
mse = 1e30
best_L = 0
alpha = 2

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
    
    #find ak, bk
    
    for L in range(1, 50): #1 to 50
        mat1 = [[0 for x in range(2*L-1)] for y in range(2*L-1)]
        for i in range(L): #0 to L-1
            for j in range(L): #0 to L-1
                for n in range(n1, n2+1): #n1 to n2
                    #w[n]
                    mat1[i][j] += float(original_data[n-i-1])*float(original_data[n-j-1])*(2*n/(n1+n2))
            for j in range(L, 2*L-1): #L to 2*L-2
                for n in range(n1, n2+1):
                    mat1[i][j] += float(original_data[n-i-1])*pow((float(original_data[n-j+L-1])-float(original_data[n-j+L-2])), alpha)*(2*n/(n1+n2))
        for i in range(L, 2*L-1): #L to 2*L-2
            for j in range(L):
                for n in range(n1, n2+1): #n1 to n2
                    mat1[i][j] += float(original_data[n-j-1])*pow((float(original_data[n-i+L-1])-float(original_data[n-i+L-2])), alpha)*(2*n/(n1+n2))
            for j in range(L, 2*L-1):
                for n in range(n1, n2+1): #n1 to n2
                    mat1[i][j] += pow((float(original_data[n-j+L-1])-float(original_data[n-j+L-2])), alpha) * pow((float(original_data[n-i+L-1])-float(original_data[n-i+L-2])), alpha)*(2*n/(n1+n2))
        mat2 = np.linalg.inv(mat1)
        mat3 = []
        for k in range(L):
            mat3.append(0)
            for n in range(n1, n2+1):
                mat3[k] += float(original_data[n])*float(original_data[n-k-1])*(2*n/(n1+n2))
        for k in range(L, 2*L-1): #L to 2*L-2
            mat3.append(0)
            for n in range(n1, n2+1):
                mat3[k] += float(original_data[n])*pow((float(original_data[n-k+L-1])-float(original_data[n-k+L-2])), alpha)*(2*n/(n1+n2))
        parameter = np.matmul(mat2, mat3)
        #print(parameter)
        #print(L)
        #calculate mse
        mse_L = 0
        for n in range(n3, n4+1): #n3 to n4
            #w[n]
            for k in range(2*L-1):
                if k<L: predict_data[n] += parameter[k]*float(original_data[n-k])
                if k>=L: predict_data[n] += parameter[k]*pow(float(original_data[n-k+L-1])-float(original_data[n-k+L-2]), alpha)
            predict_data[n]/=2
            print(f"prediction: {predict_data[n]}, practical: {original_data[n]}")
            mse_L += pow(float(original_data[n]) - predict_data[n], 2)
        
        if (mse_L < mse) & (L != 1):
            mse = mse_L
            best_L = L
            best_alpha = alpha
        print("mse_L =", mse_L)
        print("mse =", mse)
        print("L =", L)
        print("best_L =", best_L)
        print("alpha =", best_alpha)


