# import numpy as np
# arr = np.array([1, 2, 3])
# print(arr[2])


# import numpy as np
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st row: ', arr[1, 3])

# import numpy as np

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr[1, 0, 2])

# import numpy as np
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr.shape)

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 6)
# print(newarr)


# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr3 = np.array([7,8,9])
# arr = np.concatenate((arr1, arr2,arr3))
# print(arr)


# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6,7,8])
# newarr = np.array_split(arr, 3)
# print(newarr)

# import numpy as np
# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))

# import numpy as np
# arr = np.array([41, 42, 43, 44])
# x = arr[[True, True, True, False]]
# print(x)
# from numpy import random

# x = random.randint(100)

# y=random.randint(100,size=(2))
# z=random.randint(100,size=(10,3))
# print(x)
# print(y)
# print(z)
# from numpy import random

# x = random.choice([3, 5, 7, 9])

# print(x)

# from numpy import random

# x = random.choice([3, 5, 7,8,6, 9], size=(3, 5))

# print(x)

# from numpy import random

# x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

# print(x)/

import numpy as np

# arr2D = np.array([[1,2,3],
#                   [4,5,6],
#                   [7,8,9]])

# print(arr2D)
# print(arr2D.shape)


# arr1=np.zeros((2,3),dtype="int64")
# print(arr1, arr1.shape)

# arr1=np.full((2,3),100)
# print(arr1, arr1.shape)
# arr1=np.array([1,2,3,4,5,6])
# # reshaped=arr1.reshape((3,2))
# # print(reshaped,reshaped.shape)
# # idx=[0,1,2]
# # print(arr1[idx])
# x=arr1.view()
# arr1[0]=23
# print(arr1)
# print(x)

# arr1=np.array([[1,2,3],[5,6,7],[8,9,4]])
# print(arr1)
# print(np.sum(arr1))
# sum_of_col=np.sum(arr1, axis=0)
# print(arr1[0:2,1:2])

# arr=np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]])
# print(arr, arr.shape)
# print(arr[1,1,0])
# arr1=np.array([6,7,8,9,5])
# arr=np.array([1,2,3,4,5])
# print(arr ** 2)
# print(arr1 + arr)
# print()

# arr1=np.array([1,2,3,4,5],[1,2,3,4,5])
# # print()

# arr1=np.array([[1,2],[3,4]])
# mean=np.mean(arr1)
# std_dev=np.std(arr1)

# normalized_arr=(arr1-mean)/std_dev
# print(normalized_arr)
from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)

