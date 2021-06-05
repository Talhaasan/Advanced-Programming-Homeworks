#########################################################################################
# Name: Ibrahim Talha Asan
# Student ID: 64170019
# Department: Computer Engineering
#
# Assignment ID: A1
########################################################################################
#########################################################################################
# QUESTION III
# Description:
#The objective of this question is Perform a benchmark analysis of the Binary Search method.
# Sources:
#Binary Search Code :https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBinarySearch.html#analysis-of-binary-search
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION III:")
print("********************************************************************************")

import random
import time

def binarySearch(alist, item):
	    if len(alist) == 0:
	        return False
	    else:
	        midpoint = len(alist)//2
	        if alist[midpoint]==item:
	          return True
	        else:
	          if item<alist[midpoint]:
	            return binarySearch(alist[:midpoint],item)
	          else:
	            return binarySearch(alist[midpoint+1:],item)

def fillFile(fileSize,fileName):
        file = open(fileName+'.txt', 'w')
        values =[]
        for i in range(fileSize):
                value = random.randint(0,fileSize+1000)
                values.append(value)
                binarySearch(values,i)
                file.write(str(i+1)+ ' ' + str(values[i]))
                file.write('\n')
        file.close()

def readFile(fileName):
        file = open(str(fileName)+'.txt', 'r')
        values = []
        for i in file:
                values.append(i.split()[-1])
        return values

fileSizes = [1000,5000,10000,25000,50000,100000,200000]
file = open('searchStats.txt', 'w')

file.write('fillFile ')
for i in fileSizes:
        start = time.time()
        fillFile(i,'file'+str(i))
        finish = time.time()
        runtime = finish - start
        file.write(str(runtime)+' ')

file.write('\n')

file.write('readFile ')
for i in fileSizes:
        start = time.time()
        readFile('file'+str(i))
        finish = time.time()
        runtime = finish - start
        file.write(str(runtime)+' ')
file.close()