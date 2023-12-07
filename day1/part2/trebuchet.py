import re

#Parse Documents
calibrationDocument = open("day1/part2/calibrationDocument.txt", "r")

def findCalibrationValue(calibrationDocument):

    print("======START======")

    calibrationValue = 0
    numberMapping = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }

    #loop through documents
    for line in calibrationDocument:

        lineOriginal = line

        firstFindIndex = len(line) # Set max index length of line
        lastFindIndex = 0
        firstFindNumber = None
        lastFindNumber = None

        for number in numberMapping:
            index = line.find(number)
            if index  != -1 and index < firstFindIndex:
                firstFindIndex = index
                firstFindNumber = number
            if index != -1 and index > lastFindIndex:
                lastFindIndex = index
                lastFindNumber = number

        line = line.replace("\n","")
        lineOriginal = lineOriginal.replace("\n","")
        if firstFindNumber:
            line = line.replace(firstFindNumber, numberMapping[firstFindNumber])
        if lastFindNumber:
            line = line.replace(lastFindNumber, numberMapping[lastFindNumber])

        numberOnlyLine = re.sub("[^0-9]", "", line)
        firstDigit = numberOnlyLine[0]
        lastDigit = numberOnlyLine[-1]
        lineDigit = int(firstDigit + lastDigit)
        calibrationValue = calibrationValue + lineDigit
        print(lineOriginal, line, numberOnlyLine ,firstFindNumber, lastFindNumber, lineDigit, calibrationValue)

    return calibrationValue

calibrationValue = findCalibrationValue(calibrationDocument)
print(calibrationValue)