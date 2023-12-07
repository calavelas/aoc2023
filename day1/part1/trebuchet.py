import re

#Parse Documents
calibrationDocument = open("day1/calibrationDocument.txt", "r")

def findCalibrationValue(calibrationDocument):

    calibrationValue = 0

    for line in calibrationDocument:
        # Filter out non digit character
        numberOnlyLine = re.sub("[^0-9]", "", line)
        firstDigit = numberOnlyLine[0]
        lastDigit = numberOnlyLine[-1]
        lineDigit = int(firstDigit + lastDigit)
        calibrationValue = calibrationValue + lineDigit
        
        print(f'Number Only Line : {numberOnlyLine} , First Digit : {firstDigit} , Last Digit : {lastDigit} , Line Digit : {lineDigit} , Calibration Value : {calibrationValue}')

    return calibrationValue

calibrationValue = findCalibrationValue(calibrationDocument)
print(calibrationValue)