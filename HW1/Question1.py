#########################################################################################
# Name: Ibrahim Talha Asan
# Student ID: 64170019
# Department: Computer Engineering
#
# Assignment ID: A1
########################################################################################
#########################################################################################
# QUESTION I
# Description:
#The objective of this question is to generate and read files that contain a list of random numbers and
#record the run times of functions into a file named “fileStats.txt”. The “fileStats.txt”
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION I:")
print("********************************************************************************")

import random
import time

def fillFile(fileSize,fileName):

    temporaryIndex = None

    if fileSize == fileSizes[0]:
        temporaryIndex = fileSizes[0]
    elif fileSize == fileSizes[1]:
        temporaryIndex = fileSizes[1]
    elif fileSize == fileSizes[2]:
        temporaryIndex = fileSizes[2]
    elif fileSize == fileSizes[3]:
        temporaryIndex = fileSizes[3]
    elif fileSize == fileSizes[4]:
        temporaryIndex = fileSizes[4]
    elif fileSize == fileSizes[5]:
        temporaryIndex = fileSizes[5]
    elif fileSize == fileSizes[6]:
        temporaryIndex = fileSizes[6]
    else:
        print('Wrong file size !')

    if temporaryIndex != None:
        file = open(fileName + '.txt', 'w')
        while temporaryIndex > 0:
            randomNumber = random.randint(0, fileSize + 1000)
            randomNumber=randomNumber%temporaryIndex
            for i in range(int(fileSize / 10)):
                shuffledNumber = randomNumber
                file.write(str(shuffledNumber) + '\n')
                temporaryIndex -= 1
        file.close()

def readFile(fileName):
    file = open(str(fileName) + '.txt', 'r')
    values = []
    for line in file:
        values.append(line.split())
    return values

fileSizes = [1000, 5000, 10000, 25000, 50000, 100000, 200000]
fillFileRunTimes = []
readFileRunTimes = []

for i in fileSizes:
    start = time.time()
    fillFile(i, 'file' + str(i))
    finish = time.time()
    runTime = finish - start
    fillFileRunTimes.append(str(runTime))

for i in fileSizes:
    start = time.time()
    readFile('file' + str(i))
    finish = time.time()
    runTime = finish - start
    readFileRunTimes.append(str(runTime))

with open("fileStats.txt", "w") as file:
    file.write("fillFile ")
    file.write(", ".join(fillFileRunTimes))
    file.write("\nreadFile ")
    file.write(", ".join(readFileRunTimes))
