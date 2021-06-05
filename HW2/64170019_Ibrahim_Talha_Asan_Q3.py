import pandas as pd
import numpy as np

nums = pd.Series([8, 30, 39, 12, 29, 8, 25, 16, 22, 32, 15, 37, 35, 39, 26, 6])
maxValue = nums.max()
print(maxValue)
minValue = nums.min()
print(minValue)

nums1 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
nums2 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print(nums1 == nums2)
print("nums1 and nums2 series are equal")

exam_data = {'name': ['Ahmet', 'Mehmet', 'Zehra', 'Osman', 'Fatma', 'Mert', 'Cem', 'Kerem','Sevgi', 'Pınar'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data,index=labels)
print('Dataframe:\n',df)
print('\n')

selectedColumns = df.loc[:, ['name', 'score',]]
print('Name and Score Columns:\n',selectedColumns)
print('\n')
    
numberOfAttemptsIsBiggerThanTwo = df[df['attempts'] > 2]
print('Number of attempts is bigger than 2:\n', numberOfAttemptsIsBiggerThanTwo)
print('\n')

missingScoreRows =df[df['score'].isnull()]
print('Missing Score Rows:\n',missingScoreRows)
print('\n')
