import csv
import numpy as np

path = r"/Users/chinying/Desktop/ee/ee5/re/0907/data2.csv"
original_data = []

with open(path, 'r') as data:
    #trans data.csv into an array
    data_content = csv.reader(data, delimiter=',')
    next(data_content)

    for row in data_content:
        original_data.append(row[1])
    
    #L alpha norm
    alpha = input("a = ")
    sum = 0
    for i in range(0, 100):
        sum += pow(abs(float(original_data[i])), int(alpha))
    norm = pow(sum, 1/int(alpha))
    print("L(a)norm =", norm)

    y = [2, 3, 3, 4, 5, 4, 5]
    b = [[1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6, 7],
        [1, -1, 1, -1, 1, -1, 1]]
    A = np.transpose(b)
    x = np.matmul(np.linalg.inv(np.matmul(b, A)), np.matmul(b, y))
    print(x)