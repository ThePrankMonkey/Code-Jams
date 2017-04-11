# Standing Ovation Solution
# Matthew Hellmer
# 2016.04.08
#
# The logic of this solution is that it looks at each shyness level, and finds out if enough people meet that shyness index. If not, it adds a friend and checks again.
#
 
sourceFile = open('A-small-practice.in', 'r')
# sourceFile = open('A-large-practice.in', 'r')
outputFile = open('AsmallTestsResults.txt', 'w')
maxCases = sourceFile.readline().replace('\r','').replace('\n','')
print('There are %s test cases' % maxCases)
# Proceeds through each case
for case in range(int(maxCases)):
    print('Currently working on %s of %s' % (case+1, maxCases))
    # sets initial values
    friends = 0
    standing = 0
    # grabs next test case
    data = sourceFile.readline().replace('\r','').replace('\n','').split(' ')
    # splits data
    maxS = int(data[0])
    allShyLevels = data[1]
   
    # looks at each shyness level
    for shyLevel in range(maxS+1):
        # checks if the current amount of friends and already standing people can overcome the current shyness level
        while (friends + standing) < shyLevel:
            # increase friend count by 1, and checks again
            friends += 1
        # once you have enough folks standing, add the current shyness level's group to those standing
        standing += int(allShyLevels[shyLevel])
   
    # write to the output file
    outputFile.write('Case #%s: %s\n' % (case+1, friends))
 
# close the open files
sourceFile.close()
outputFile.close()
