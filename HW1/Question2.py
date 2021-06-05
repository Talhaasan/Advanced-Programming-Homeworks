#########################################################################################
# Name: Ibrahim Talha Asan
# Student ID: 64170019
# Department: Computer Engineering
#
# Assignment ID: A1
########################################################################################
#########################################################################################
# QUESTION II
# Description:
#The objective of this question is perform a benchmark analysis of the sorting algorithms and
#record the execution time of each sorting algorithm into a file named “sortStats.txt”.
# Sources:
#Bubble Sort Code :https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBubbleSort.html
#Selection Sort Code :https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheSelectionSort.html
#Insertion Sort Code :https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html
#Shell Sort Code :https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheShellSort.html
#Merge Sort Code :https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
#Quick Sort Code :https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html
#Heap Sort Code :I did not find this sorting algorithm code on lecture notes and I take code on;
#https://www.geeksforgeeks.org/python-program-for-heap-sort/
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION II:")
print("********************************************************************************")

def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


import numpy as np
import time
import random

bubbleSort_result = []
selectionSort_result = []
insertionSort_result = []
shellSort_result = []
mergeSort_result = []
quickSort_result = []
heapSort_result = []

fileSizes = [1000, 5000, 10000, 25000, 50000, 100000, 20000]
fileName = "sortStats.txt"

for i in fileSizes:

    randomList = random.sample(range(1, 100500), i)

    array = np.array(randomList)
    start = time.time()
    bubbleSort(array)
    end = time.time()
    bubbleSort_result.append(round((end - start), 5))

    array = np.array(randomList)
    start = time.time()
    selectionSort(array)
    end = time.time()
    selectionSort_result.append(round((end - start), 5))

    array = np.array(randomList)
    start = time.time()
    insertionSort(array)
    end = time.time()
    insertionSort_result.append(round((end - start), 5))

    array = np.array(randomList)
    start = time.time()
    shellSort(array)
    end = time.time()
    shellSort_result.append(round((end - start), 5))

    array = np.array(randomList)
    start = time.time()
    mergeSort(array)
    end = time.time()
    mergeSort_result.append(round((end - start), 5))

    array = np.array(randomList)
    start = time.time()
    quickSort(array)
    end = time.time()
    quickSort_result.append(round((end - start), 5))

    array = np.array(randomList)
    start = time.time()
    heapSort(array)
    end = time.time()
    heapSort_result.append(round((end - start), 5))

    file = open(fileName, 'w')
    row1 = "Bubble Sort "
    row2 = "Selection Sort "
    row3 = "Insertion Sort "
    row4 = "Shell Sort "
    row5 = "Merge Sort "
    row6 = "Quick Sort "
    row7 = "Heap Sort "

    file.write(row1)
    file.write(str(bubbleSort_result))
    file.write('\n')
    file.write(row2)
    file.write(str(selectionSort_result))
    file.write('\n')
    file.write(row3)
    file.write(str(insertionSort_result))
    file.write('\n')
    file.write(row4)
    file.write(str(shellSort_result))
    file.write('\n')
    file.write(row5)
    file.write(str(mergeSort_result))
    file.write('\n')
    file.write(row6)
    file.write(str(quickSort_result))
    file.write('\n')
    file.write(row7)
    file.write(str(heapSort_result))
    file.write('\n')
    file.close()
