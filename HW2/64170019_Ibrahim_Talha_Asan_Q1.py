import numpy as np

#Q1.1 and Q1.2
totalArray=np.arange(81).reshape(9,9)
for i in range(1):
    for j in range(0,9):
        a=1
        b=2
        c=3
        d=4
        e=5
        f=6
        g=7
        h=8
        k=9
        array = np.array([a+j,b+2*j,c+3*j,d+4*j,e+5*j,f+6*j,g+7*j,h+8*j,k+9*j])    
        totalArray[j]=array
    print('Q1.1')
    print(totalArray)
    print('Q1.2')
    totalArray[totalArray%2==1] = -1
    print(totalArray)

print('Q1.3')
prog = np.array([1,2,3,4,6])
prog2=np.array(np.repeat(prog[0],8))
prog3=np.array(np.repeat(prog[1],8))
prog4 = np.concatenate((prog2, prog3))
prog5=np.array(np.repeat(prog[2],8))
prog6 = np.concatenate((prog4, prog5))
prog7=np.array(np.repeat(prog[3],8))
prog8 = np.concatenate((prog6, prog7))
prog9=np.array(np.repeat(prog[4],8))
prog10 = np.concatenate((prog8, prog9))

for i in range(4):
    prog11=np.array(prog)
    print(prog11)
prog12 = np.concatenate((prog10, prog11))
prog13 = np.concatenate((prog12, prog11))
prog14 = np.concatenate((prog13, prog11))
prog15 = np.concatenate((prog14, prog11))
print(prog15)
  
print('Q1.4')  
array1 = np.random.randint(0,10, size=(1,15))
array2 = np.random.randint(0,10, size=(1,15))
print(array1)
print(array2)
print(np.intersect1d(array1, array2))

print('Q1.5')
for _ in range(50):
    randomNumber = np.random.randint(0,150)
    if randomNumber > 100:
        randomNumber = 100
    elif randomNumber < 50:
        randomNumber = 50
    print(randomNumber)  
print('\n')

print('Q1.6')
array1 = np.random.randint(100, size=16) 
array1 = np.resize(array1, (4,4)) 

array2 = np.random.randint(100, size=16)
array2 = np.resize(array2, (4,4))

array3 = np.random.randint(100, size=16)
array3 = np.resize(array3, (4,4)) 

print('Array 1:\n',array1)
print('\n') 
print('Array 2: \n',array2)
print('\n')
print('Array 3: \n',array3)
print('\n')

summation_arrays = array1 + array2 + array3
avarage_summation_array = summation_arrays/3
avarage_summation_array = np.round(avarage_summation_array, 2)

print('Avarage array:\n',avarage_summation_array)
print('\n')  

rowNumber = 0

for i in avarage_summation_array:
  print("Array's",rowNumber, 'row stats')           
  print('Maximum :', np.round(np.amax(i),2)) 
  print('Minimum :', np.round(np.amin(i),2))
  print('Mean :', np.round(np.mean(i))) 
  print('Standard Deviation :',np.round(np.std(i)))
  print('\n')  
  
  rowNumber=rowNumber+1    
  