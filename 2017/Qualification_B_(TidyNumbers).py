import time

inputFile = open('B-small-attempt1.in', 'r')
#inputFile = open('B-sample.in', 'r')
outputFile = open('B-small-answer.in', 'w')

def CheckNumber(number):
    numString = str(number)
    numList = list(numString)
    numList.sort()
    numOrdered = "".join(numList)
    return numString == numOrdered

def GetAnswer(number):
    while number > 0:
        results = CheckNumber(number)
        if results:
            return str(number)
        number -= 1
    return str(number)

def BuildAnswerFile():
    entries = int(inputFile.readline())
    count = 0
    for line in range(entries):
        count += 1
        currentVal = int(inputFile.readline())
        if currentVal:
            #print("Working with", currentVal)
            answer = GetAnswer(currentVal)
            lineAnswer = "Case #" + str(count) + ": " + str(answer) + "\r"
            outputFile.write(lineAnswer)

t0 = time.time()
BuildAnswerFile()
t1 = time.time()
td = t1-t0
print("\r\n\r\nIt took %.2f seconds" % td)

outputFile.close()

print("\r\n\r\n!!!! Done !!!!")
