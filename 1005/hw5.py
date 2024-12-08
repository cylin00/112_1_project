import csv
import numpy as np

path = r"/Users/chinying/Desktop/ee/ee5/re/0907/data2.csv"

original_data = []
predict_data = []
parameter = []
n1, n2, n3, n4 = 50, 199, 200, 251
mse = 1e30
best_M = 0
t=2
#w[n] = (2*n/(n1+n2))

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
        predict_data[i] = 0
    #original_data = original_data.astype('float64')
    
    t = input("without weight -> input:0 ; with weight -> input:1 =>")
    
    #find ak, bk
    
    for M in range(1, 50): #1 to 50
        
        if(int(t)==0):
            
            mat1 = [[0.0 for x in range(0, M+1)] for y in range(0, M+1)]
            for s in range(0, M+1):
                for k in range(0, M+1):
                    for n in range(n1, n2+1):
                        mat1[s][k] = mat1[s][k] + 2*pow(n, k)*pow(n, s)
            
            mat2 = np.linalg.inv(mat1)
            
            mat3 = []
            for s in range(0, M+1):
                mat3.append(0)
                for n in range(n1, n2+1):
                    mat3[s] = mat3[s] + 2*float(original_data[n])*pow(n, s)
            
            parameter = np.matmul(mat2, mat3)


        if(int(t)==1):
            print("in&&")
            mat1 = [[0.0 for x in range(0, M+1)] for y in range(0, M+1)]
            for s in range(0, M+1):
                for k in range(0, M+1):
                    for n in range(n1, n2+1):
                        mat1[s][k] = mat1[s][k] + 2*(2*n/(n1+n2))*pow(n, k) * pow(n, s)
            
            mat2 = np.linalg.inv(mat1)

            mat3 = []
            for s in range(0, M+1):
                mat3.append(0)
                for n in range(n1, n2+1):
                    mat3[s] = mat3[s] + 2*(2*n/(n1+n2))*float(original_data[n])*pow(n, s)
            
            parameter = np.matmul(mat2, mat3)

        
        #print(parameter)
        #print(L)
        #print("M = ", M)

        #calculate mse
        mse_M = 0
        for n in range(n3, n4+1): #n3 to n4
            #predict_data.append(0)
            for k in range(0, M+1):###
                predict_data[n] = predict_data[n] + parameter[k]*pow(n, k) #out of range
            predict_data[n]/=2
            if(M==5):print(f"prediction: {predict_data[n]}, practical: {original_data[n]}")
            mse_M = mse_M+ pow(float(original_data[n]) - predict_data[n], 2)
        
        if (mse_M < mse) & (M != 1):
            mse = mse_M
            best_M = M
        print("mse_M =", mse_M)
        print("mse =", mse)
        print("M =", M)
        print("best_M =", best_M)


