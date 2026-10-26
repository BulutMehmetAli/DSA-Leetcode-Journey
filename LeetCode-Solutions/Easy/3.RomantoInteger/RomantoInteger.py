symbolDict = {"I" : 1 , "V" : 5 , "X" : 10 , "L" : 50 , "C" : 100 , "D" : 500 , "M" : 1000}

inputValue = "MCMXCIV"
sizeOfInput = len(inputValue)
# print(symbolDict[inputValue[0]])
sum = 0
for i in range(sizeOfInput):
    if (i + 1 < len(inputValue) and (symbolDict[inputValue[i]] < symbolDict[inputValue[i+1]])) :
        sum -= symbolDict[inputValue[i]]
    else:
        sum += symbolDict[inputValue[i]]
print(sum)