import math as math
from fractions import Fraction

listOfFractions = []

def stringToFracList(s): # Take in a string s and turn it into a fraction list, [numerator, denominator].
    if '/' in s: # One case, if the string is a ratio of integers.
        testList = s.split('/')
        for i in range(len(testList)):
            try:
                int(testList[i])
            except:
                return
            else:
                testList[i] = int(testList[i])
        fraction = Fraction(testList[0], testList[1])
        testList[0] = fraction.numerator
        testList[1] = fraction.denominator
        return testList
    elif '.' in s: # Second case, if the string is a decimal number.
        try:
            float(s)
        except:
            return
        else:
            fraction = Fraction(float(s)).limit_denominator()
            testList = [int(fraction.numerator), int(fraction.denominator)]
            return testList
    else: # I did not bother implementing the case where the string is a regular integer.
        return

def firstPart(x, y): # First term in the algorithm.
    num = 1
    den = math.ceil(y/x)
    return [num, den]

def secondPart(x, y): # Second term in the algorithm.
    num = -y % x
    den = y*math.ceil(y/x)
    return [num, den]

def fibAlg(): # This function does the repetition of the Fibonacci algorithm, until our final fraction has numerator 1 or 0.
    if type(listOfFractions[-1]) != type([]):
        return
    while listOfFractions[-1][0] != 1 and listOfFractions[-1][0] != 0:
        tempFrac = listOfFractions[-1]
        listOfFractions.pop()
        listOfFractions.append(firstPart(tempFrac[0], tempFrac[1]))
        listOfFractions.append(secondPart(tempFrac[0], tempFrac[1]))

def listsToString(myList): # Once the algorithm is done, we turn our list of fractions into a single string.
    stringList = []
    finalString = ""
    for i in myList:
        stringList.append(str(i[0]) + "/" + str(i[1]))
    for i in stringList:
        finalString += i + " + "
    return(finalString[:-3])

def main():
    startFrac = stringToFracList(input("What fraction would you like to use? "))
    listOfFractions.append(startFrac)
    if len(listOfFractions) == 0:
        print("Input must be written as a ratio of integers or a decimal number.")
        return
    fibAlg()
    if type(listOfFractions[-1]) != type([]):
        print("Input must be written as a ratio of integers or a decimal number.")
        return
    elif listOfFractions[-1][0] == 0:
        print("Your fraction can be written as " + listsToString(listOfFractions[:-1]) + ".")
    else:
        print("Your fraction can be written as " + listsToString(listOfFractions) + ".")
main()