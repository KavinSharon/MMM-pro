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
newData.sort()
if n % 2 == 0 :
    median1 = float(newData[n//2])
    median2 = float(newData[n//2-1])
    median = (median1+median2)/2
else:
    median = float(newData[n//2])

print("Median Is "+str(median))