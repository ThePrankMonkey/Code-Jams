import time

inputFile = open('C-small-practice-2.in', 'r')
#inputFile = open('C-sample.in', 'r')
outputFile = open('C-small-answer.in', 'w')

def GetAnswer(inString):
    n, k = inString.split(" ")
    stallString = "o" + int(n)*"e" + "o"
    users = int(k)
    #print("Stalls:", stallString, "\rUsers:", users)
    for i in range(users):
        # Find LS and RS for all spots
        findings = [] # index, LS, RS, Min, Max
        maxMinFound = 0
        for j in range(len(stallString)):
            if stallString[j] == "e":
                temp = []
                temp.append(j)
                # Find LS
                leftChunk = stallString[:j][::-1]
                LS = leftChunk.index("o")
                temp.append(LS)
                # Find RS
                rightChunk = stallString[(j+1):]
                RS = rightChunk.index("o")
                temp.append(RS)
                # Find Min
                tempMin = min(LS,RS)
                if tempMin > maxMinFound:
                    maxMinFound = tempMin
                temp.append(tempMin)
                # Find Max
                tempMax = max(LS,RS)
                temp.append(tempMax)
                # Collect everything
                findings.append(temp)
        # Pull out the ones that have the biggest Min
        reducedFindings = [] # index, LS, RS, Min, Max
        maxMaxFound = -1
        for j in range(len(findings)):
            if findings[j][3] == maxMinFound:
                reducedFindings.append(findings[j])
                if findings[j][4] > maxMaxFound:
                    maxMaxFound = findings[j][4]
        #print("reducedFindings", reducedFindings)
        # Pull out the ones that have the biggest Max
        furtherReducedFindings = [] # index, LS, RS, Min, Max
        for j in range(len(reducedFindings)):
            if reducedFindings[j][4] == maxMaxFound:
                furtherReducedFindings.append(reducedFindings[j])
        #print("furtherReducedFindings", furtherReducedFindings)
        # Take the first one and update it's spot in the stallString
        try:
            lastPerson = furtherReducedFindings[0]
            lastPersonIndex = lastPerson[0]
            tempStallString = list(stallString)
            tempStallString[lastPersonIndex] = "o"
            stallString = "".join(tempStallString)
        except:
            lastPerson = ["", "", "", "Error", "There Was"]
            print("error")
        #print("New String:", stallString)
    
    return str(lastPerson[4]) + " " + str(lastPerson[3])

def BuildAnswerFile():
    entries = int(inputFile.readline())
    count = 0
    for line in range(entries):
        count += 1
        currentVal = inputFile.readline()
        if currentVal:
            #print("Working with", currentVal)
            answer = GetAnswer(currentVal)
            lineAnswer = "Case #" + str(count) + ": " + str(answer) + "\r"
            print(lineAnswer)
            outputFile.write(lineAnswer)

t0 = time.time()

BuildAnswerFile()
t1 = time.time()

td = t1-t0
print("\r\n\r\nIt took %.2f seconds" % td)

outputFile.close()

print("\r\n\r\n!!!! Done !!!!")
