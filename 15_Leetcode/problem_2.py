'''
Given a sorted array of distinct integers and a target value, return the index if the target is found.
 If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
 

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2
    
Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4
'''

def searchInsert(nums, target):
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
        mid = (left + right) // 2
        # if target number is found, return
        if nums[mid] == target:
            return mid
        # [1,3,5,6] target 7
        # if number is smaller than the target num
        elif nums[mid] < target:
            # if the mid pointer meets the right pointer, return mid + 1 index
            if mid == right:
                return mid + 1
            else:
                # move the left pointer
                left = mid + 1
        # if number is bigger than the target num
        else:
            # if the mid pointer meets the left pointer, return mid
            if mid == left:
                return mid
            # move the right pointer 
            else:
                right = mid - 1
