s = "aaaaaa"
t = "bbaaaa"

newString = ""
bCounter = 0

for aCount, aValue in enumerate(s):
    
    for bCount in range (bCounter, len(t)):

        if aValue == t[bCount]:
            newString += t[bCount]
            bCounter += 1  
            break

        bCounter += 1


print(newString)
        

    