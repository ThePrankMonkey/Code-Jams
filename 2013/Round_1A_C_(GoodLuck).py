# datain = open('C-test-practice.in', 'r')
datain = open('C-small-practice-1.in', 'r')
# datain = open('C-small-practice-2.in', 'r')

dataout = open('dataout.txt', 'w')

def makeGuessList(values, maxValue):
    guessList = []
    for i1 in range(2,maxValue+1):
        if values == 1:
            guessList.append(str(i1))
        for i2 in range(2,maxValue+1):
            if values == 1:
                break
            if values == 2:
                guessList.append(str(i1)+str(i2))
            for i3 in range(2,maxValue+1):
                if values == 2:
                    break
                if values == 3:
                    guessList.append(str(i1)+str(i2)+str(i3))
                for i4 in range(2,maxValue+1):
                    if values == 3:
                        break
                    if values == 4:
                        guessList.append(str(i1)+str(i2)+str(i3)+str(i4))
                    for i5 in range(2,maxValue+1):
                        if values == 4:
                            break
                        if values == 5:
                            guessList.append(str(i1)+str(i2)+str(i3)+str(i4)+str(i5))
                        for i6 in range(2,maxValue+1):
                            if values == 5:
                                break
                            if values == 6:
                                guessList.append(str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6))
                            for i7 in range(2,maxValue+1):
                                if values == 6:
                                    break
                                if values == 7:
                                    guessList.append(str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i7))
                                for i8 in range(2,maxValue+1):
                                    if values == 7:
                                        break
                                    if values == 8:
                                        guessList.append(str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i7)+str(i8))
                                    for i9 in range(2,maxValue+1):
                                        if values == 8:
                                            break
                                        if values == 9:
                                            guessList.append(str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i7)+str(i8)+str(i9))
                                        for i10 in range(2,maxValue+1):
                                            if values == 9:
                                                break
                                            if values == 10:
                                                guessList.append(str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i7)+str(i8)+str(i9)+str(i10))
                                            for i11 in range(2,maxValue+1):
                                                if values == 10:
                                                    break
                                                if values == 11:
                                                    guessList.append(str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i7)+str(i8)+str(i9)+str(i10)+str(i11))
                                                for i12 in range(2,maxValue+1):
                                                    if values == 11:
                                                        break
                                                    if values == 12:
                                                        guessList.append(str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i7)+str(i8)+str(i9)+str(i10)+str(i11)+str(i12))
    return guessList

def makeProductList(guessList, values):
    binList = [bin(x)[2:].zfill(values) for x in range(2**values)]
    productList = []
    for i in guessList:
        productListSub = []
        for j in binList:
            value = 1
            for k in range(values):
                value *= max(int(i[k])*int(j[k]),1)
            productListSub.append(value)
        productList.append(productListSub)
    return productList

def findAnswer(productList, herProducts, guessList):
    for i in productList:
        i.extend([1]*len(herProducts))
    for i in herProducts:
        for j in productList:
            if i in j:
                j.remove(i)
            else:
                j.extend([0]*10)
    countList = []
    for i in productList:
        countList.append(len(i))
#     print countList 
    fewestValuesIndex = countList.index(min(countList))
    return guessList[fewestValuesIndex]

length = int(datain.readline())
dataout.write('Case #' + str(length) + ':\n')

rVal, values, maxValue, kVal = map(int, datain.readline().split())

guessList = makeGuessList(values, maxValue)
productList = makeProductList(guessList, values)

print guessList
print productList

for i in range(rVal):
    print 'working on ' + str(i+1) + ' of ' + str(rVal)
    productList = makeProductList(guessList, values)
    herProducts = map(int, datain.readline().split())
    answer = findAnswer(productList, herProducts, guessList)
#     print '    best guess on ' + str(herProducts) + ' is ' + str(answer)
    dataout.write(str(answer) + '\n')

print guessList
print productList

datain.close()
dataout.close()
