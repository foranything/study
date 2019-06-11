import random
import math

arr = [random.randrange(1, 101) for i in range(10)]
print(arr)
def merge_sort(arr):
  
  arr1 = arr[:math.floor((len(arr))/2)]
  arr2 = arr[math.floor((len(arr))/2):]
  if not len(arr1) == 0:
    arr1 = merge_sort(arr1)
  if not len(arr2) == 1:
    arr2 = merge_sort(arr2)
  return merge(arr1, arr2)

def merge(arr1, arr2):
  arr = []
  while len(arr1) > 0 and len(arr2) > 0:
    if arr1[0] < arr2[0]:
      arr.append(arr1.pop(0))
    else:
      arr.append(arr2.pop(0))
  if len(arr1) == 0:
    arr.extend(arr2)
  else:
    arr.extend(arr1)
  return arr

print(merge_sort(arr))