import numpy as np

def readMatrix(file):
   matrix = []
   for row in range(4):
       matrix.append([])
       line = file.readline()
       rowdata = [int(x) for x in line.split(' ')]
       for column in range(4):
           matrix[row].append(rowdata[column])
   return matrix

f = open("inputs.txt","r") 

line = f.readline()  
A = readMatrix(f)
A = np.array(A)
print(" ***** Matrix A ***** ")
print(A)
print('\n')

line = f.readline()
B = readMatrix(f)
B = np.array(B)
print(" ***** Matrix B ***** ")
print(B) 
print('\n')

line = f.readline()
C = readMatrix(f)
C = np.array(C)
print(" ***** Matrix C ***** ")
print(C) 
print('\n')

print(" ***** Matrix D ***** ")
D = np.random.randint(100, size=16) 
D = np.resize(D, (4,4))
print(D)
print('\n')

print("\n *** Computing S = (A+B) * Transpose(C) + D - A ***\n")

T1 = A + B
print(" ***** Matrix T1 = (A+B) *****")
print(T1)
print('\n')

T2 = np.transpose(C)
print(" ***** Matrix T2 = Transpose(C) *****")
print(T2)
print('\n')

T3 = T1.dot(T2)
print(" ***** Matrix T3 = (A+B)*Transpose(C) *****")
print(T3) 
print('\n')

T4 = T3 + D
print(" ***** Matrix T4 = (A+B)*Transpose(C) + D *****")
print(T4)
print('\n') 


S = T4-A
print(" ***** Matrix S = (A+B)*Transpose(C) + D - A *****")
print(S)
print('\n')

maxValueOfSMatrix = np.amax(S)
print("Maxium Element in S = ",maxValueOfSMatrix)

f.close() # closing file  

