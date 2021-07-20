from collections import Counter
import csv
with open('pro/heightWeight.csv',newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    noOfLines = fileData[i][2]
    newData.append(float(noOfLines))

data = Counter(newData)
dataForRange = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}

for height,occurance in data.items():
    if 75<float(height)<85:
        dataForRange["75-85"]+=occurance
    elif 85<float(height)<95:
        dataForRange["85-95"]+=occurance
    elif 95<float(height)<105:
        dataForRange["95-105"]+=occurance
    elif 105<float(height)<115:
        dataForRange["105-115"]+=occurance
    elif 115<float(height)<125:
        dataForRange["115-125"]+=occurance
    elif 125<float(height)<135:
        dataForRange["125-135"]+=occurance
    elif 135<float(height)<145:
        dataForRange["135-145"]+=occurance
    elif 145<float(height)<155:
        dataForRange["145-155"]+=occurance
    elif 155<float(height)<165:
        dataForRange["155-165"]+=occurance
    elif 165<float(height)<175:
        dataForRange["165-175"]+=occurance        
modeRange,modeOccurance = 0,0
for range,occurance in dataForRange.items():
    if occurance>modeOccurance:
        modeRange,modeOccurance = [int(range.split("-")[0]),int(range.split("-")[1])],occurance

mode = float((modeRange[0]+modeRange[1])/2)

print("The Mode Is "+str(mode))


