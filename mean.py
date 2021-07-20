import csv
with open('pro/heightWeight.csv',newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    noOfLines = fileData[i][2]
    newData.append(float(noOfLines))

n = len(newData)
total = 0
for x in newData:
    total = total+x

mean = total/n
print("The Mean Is "+str(mean))