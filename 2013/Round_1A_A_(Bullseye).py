# datain = open('A-test-practice.in', 'r')
datain = open('A-small-attempt0.in', 'r')
# datain = open('A-large.in', 'r')
dataout = open('dataout.txt', 'w')

for length in xrange(1, int(datain.readline()) + 1):

    rVal, tVal = map(long, datain.readline().split())
    
    count = 0
    
    while tVal > 0:
        tVal -= ((rVal+1)**2 - rVal**2)
        if tVal >= 0:
            count += 1
        rVal += 2
#     print 'Case', length, 'count', count
    
    dataout.write('Case #' + str(length) + ': ' + str(count) + '\n')

datain.close()
dataout.close()
