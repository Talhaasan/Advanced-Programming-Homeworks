#########################################################################################
# Name: Ibrahim Talha Asan
# Student ID: 64170019
# Department: Computer Engineering
#
# Assignment ID: A1
########################################################################################
#########################################################################################
# QUESTION V
# Description:
#The objective of this question is given orthogonal triangle input and find the maximum sum of the
#numbers according to given rules.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION V:")
print("********************************************************************************")

file = open('orthogonalTriangleInput.txt', "r")
maximumSummation = 0
isPrimeNumber = False

for row in file:
    triangleInputs = row.strip()
    triangleInputs = triangleInputs.split()

    for i in range(0, len(triangleInputs)):
        triangleInputs[i] = int(triangleInputs[i])

    for i in triangleInputs:
        for j in range(2, i):
            if (i % j) == 0:
                isPrimeNumber = True
    maximumSummation += i

print("Maximum summation is :", maximumSummation)
