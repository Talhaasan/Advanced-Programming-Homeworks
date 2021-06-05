#########################################################################################
# Name: Ibrahim Talha Asan
# Student ID: 64170019
# Department: Computer Engineering
#
# Assignment ID: A1
########################################################################################
#########################################################################################
# QUESTION IV
# Description:
#The objective of this question is using nested loops, write the code of given triangularshape.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION IV:")
print("********************************************************************************")

rows = 10
temp = rows
for i in range(1, rows):
    for j in range(temp,0,-1):
        print(end='  ')
    for j in range(0,i -1, 1):
        print(2 ** j, end=' ')
    for j in range(i-1, -1, -1):
        print(2 ** j, end=' ')
    temp = temp -1
    print("")
