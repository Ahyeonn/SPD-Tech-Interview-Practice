'''
Given an array a of n nubmers and a count k find the k largest values in the array a.

<Example>
a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]
a=[1], k = 2 -> None
'''
from collections import deque

def main(arr, k):
    sorted_arr = sorted(arr)
    return sorted_arr[-k:]

if __name__ == "__main__":
    print(main([5, 1, 3, 6, 8, 2, 4, 7], 3))