import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# array[start:end:step]
print(array[0])
print(array[1])
print(array[2])
print(array[3])



print(20 * "=","row selection",20* "=")
print("=====================================================")

print(array[0:3])
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(array[1:4])
print(50*"=")

print(array[0:4:2])

print(20 * "=","Column selection",20* "=")

print(array[:,0])
print(array[:,2])
print(array[:,0:3])
print(array[:,1:3])

print(array[:,1::2])

print(array[:,::-1])
print(array[:,::-2])


# if we want first 2 rows and first two columns so 
print(array[0:2,0:2])
print(array[0:2,2:4])