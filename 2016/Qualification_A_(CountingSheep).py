# Counting Sheep Solution
# Matthew Hellmer
# 2016.04.09
#
# The method for this solution is making a list for each digit, then going 
#   through each number as a string and looking accruing a count of each digit. 
#   Once all digits have at least one count recording, it breaks. To check for 
#   insomnia cases, I assume that all numbers will eventually be seen as long as 
#   the number changes.
#

sampleInput = '''5
0
1
2
11
1692'''.split('\n')

# fileSource = open('A-small.in', 'r')
# fileOutput = open('results.txt', 'w')

# maxCases = int(fileSource.read().replace('\n', '').replace('\r', ''))
maxCases = int(sampleInput[0])

for i in range(1,maxCases+1):
	numbers = [0]*10
	initialNum = int(sampleInput[i])
	# initialNum = int(fileSource.read().replace('\n', '').replace('\r', ''))
	# print('initialNum is: %s' % initialNum)
	currentNum = initialNum
	lastNum = 0
	while min(numbers) == 0:
		#print('number set: %s' % numbers)
		for num in str(currentNum):
			numbers[int(num)]+=1
		lastNum = currentNum
		currentNum += initialNum
		if lastNum == currentNum:
			lastNum = 'INSOMNIA'
			numbers=[1]*10
	statement = 'Case %s: %s' % (i, lastNum)
	print(statement)
	# fileOutput.write(statement)

# fileSource.close()
# fileOutput.close()
