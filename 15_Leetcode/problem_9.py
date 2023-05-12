'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.
'''
from collections import Counter

def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    # Count nums_1 and nums_2's int values as key, count_val in dic
    nums_1 = Counter(nums1)
    nums_2 = Counter(nums2)
    ans = []

    # Iterate nums_1 and check if the iterated num is in nums_2
    for i in nums_1:
        # if exists, add it to the array
        if i in nums_2:
            ans.append(i)
    return ans

