'''
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1
'''

def search( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # start from 0 index upto length of the nums
    left = 0
    right = len(nums) - 1

    # while the left pointer doesn't go above the right pointer
    while left <= right:
        # set mid value
        mid = (left+right) // 2
        # if target is found, return
        if nums[mid] == target:
            return mid
        # if target is bigger number than the mid, move the left pointer
        elif nums[mid] < target:
            left = mid + 1
        # if target is smaller number than the mid, move the right pointer
        else:
            right = mid - 1
    return -1