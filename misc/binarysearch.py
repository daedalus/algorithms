# Author Dario Clavijo 2024.

def binary_search(A, key, low, high):
  if len(A) > 0:
    mid = low + ((high - low) >> 1);
    if A[mid] > key:
      return binary_search(A, key, low, mid - 1)
    elif A[mid] < key:
      return binary_search(A, key, mid + 1, high)
    else:
      return mid


def main():
  arr = list(range(1024**2))
  assert binary_search(arr, 1337, 0, len(arr)) == 1337 
  print("binary_search OK")

if __name__ == "__main__": main()

