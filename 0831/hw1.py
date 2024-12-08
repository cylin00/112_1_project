import csv
path = r"/Users/chinying/Desktop/ee/ee5/re/0831/practice/data.csv"
original_data = []
predict_data = []

with open('data.csv', 'r') as data:
    #trans data.csv into an array
    data_content = csv.reader(data, delimiter=',')
    next(data_content)

    for row in data_content:
        original_data.append(row[1])
        #predict data
        predict_data.append(row[1])
    predict_data.pop(251)
    original_data.pop(0)

#print(original_data)
#print(predict_data)

#calculate mean square error
mse = 0
for k in range(len(predict_data)):
    mse += pow((float(predict_data[k])-float(original_data[k])), 2)
print('MSE =', mse/len(predict_data))