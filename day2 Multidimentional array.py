import numpy as np

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['S','T','U'],['V','W','X'],['Y','Z', ' ']]])

print(array.ndim)
print(array.shape)
print(array[0][0][2]) # this is known as chain indexing (slower) 
print(array[0, 0, 2]) #this is multi dimention indexing (Faster)

word = array[1, 1, 0] + array[2, 0, 2] + array[0, 1, 0] + array[0, 1, 0] + array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0] + array[0, 2, 2] + array[1, 2, 2]
print(word)