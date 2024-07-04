# Author: Dario Clavijo 2024.
# All implementations are based on the respective wikipedia articles.


def bubble_sort(arr):
  n = len(arr)
  for i in range(0, n-1):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1],arr[j]
  return arr


def merge(left,right):
  result = []
  while len(left) > 0 and len(right) > 0:
    if left[0] <= right[0]:
      result.append(left[0])
      left = left[1:]
    else:
      result.append(right[0])
      right = right[1:]
  if len(left) > 0:
    result += left[1:]
  if len(right) > 0:
    result += right[1:]
  return result


def merge_sort(arr):
  n = len(arr)
  if n <= 1: return arr
  middle = n >> 1
  left = [arr[x] for x in range(0, middle)]
  right = [arr[x] for x in range(middle, n)]
  left = merge_sort(left)
  right = merge_sort(right)
  if left[-1] <= right[0]:
    return left + right
  return merge(left, right)


def partition(arr, lo, hi):
  pivot = arr[lo]
  i = lo
  for j in range(lo, hi):
    if arr[j] >= pivot:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
  arr[hi], arr[i] = arr[i],arr[hi]
  return i


def _quick_sort(arr, lo, hi):
  if lo >= hi or lo < 0: return
  p = partition(arr, lo, hi)
  _quick_sort(arr, lo, p - 1)
  _quick_sort(arr, p + 1, hi)

  
def quick_sort(arr):
  _quick_sort(arr, 0, len(arr) - 1)
  return arr


def insertion_sort(arr):
  i = 1
  while i < len(arr):
    j=i
    while j >0 and arr[j-1] > arr[j]:
      arr[j],arr[j-1] = arr[j-1],arr[j]
      j -= 1
    i+=1
  return arr


def bitonic_sort(arr):
  n,k = len(arr), 2
  while k <= n:
    j = k >> 1
    while j > 0:
      for i in range(0, n):
        if (l:=(i^j)) > i:
          if ( (i & k) == 0 ) and ( arr[i] > arr[l] ):
             arr[i], arr[l] = arr[l], arr[i]
          if ( (i & k) != 0 ) and ( arr[i] < arr[l] ):
             arr[i], arr[l] = arr[l], arr[i]
      j >>= 1
    k <<= 1
  return arr


def odd_even_sort(arr):
  sorted = False
  while not sorted:
    sorted = True
    for i in range(1, len(arr)-1, 2):
      if arr[i] > arr[i+1]:
        arr[i],arr[i+1] = arr[i+1],arr[i]
        sorted = False
    for i in range(0, len(arr)-1, 2):
      if arr[i] > arr[i+1]:
        arr[i],arr[i+1] = arr[i+1],arr[i]
        sorted = False
  return arr


def main():
  arr = [4,1,3,6,8,5,2,9,7,0,15,13,14,10,12,11]


  s = sorted(arr)
  for f in [bubble_sort, merge_sort, quick_sort, insertion_sort, bitonic_sort, odd_even_sort]:
    assert f(arr) == s
    print(f.__name__, "OK")


if __name__ == "__main__": main()
