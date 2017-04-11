data = [6, 3]

JamLength = data[0]
JamCount = data[1]

possibleJams=[]
foundJams=[]
PossibleJamMin = 10**(JamLength-1) + 1
PossibleJamMax = int('1'*JamLength)

print(PossibleJamMin, PossibleJamMax)

def FindFactors(n):
	for i in range(2,n-1):
		if n%i == 0:
			return n
	return 0

print(FindFactors(16))

def BaseCheck(n, base):
	total=0
	strN = str(n)
	for i in reversed(range(len(strN))):
		total += int(strN[i])*base**i
	return total
	
print(BaseCheck(PossibleJamMax, 9))

def toBin(n):
	b = ''
	while n > 0:
		if n%2 == 1:
			b = '1' + b
		else:
			b = '0' + b
		n = n//2
	return b

low  = BaseCheck(PossibleJamMin,2)
high = BaseCheck(PossibleJamMax,2)
for i in range(low, high+1, 2):
	possibleJams.append(int(toBin(i)))
print(possibleJams)

RealCoinJams = []

for jam in possibleJams:
	jamArr = []
	for i in range(2,11):
		jamArr.append(BaseCheck(jam, i))
	#print(jamArr)
	testArr = []
	for test in jamArr:
		testArr.append(FindFactors(test))
	if min(testArr) > 0:
		print(testArr[-1])
		RealCoinJams.append(testArr[-1])

print(RealCoinJams[0:JamCount])
