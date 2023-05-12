'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
'''
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    # if strs is empty, return ''
    if not strs:
        return ""
    # grab the shortest str from strs
    shortest = min(strs,key=len)

    # Iterate index and the key value of shortest
    for i, ch in enumerate(shortest):
        # Iterate through word in strs
        for other in strs:
            # if the alphabet is not equal to the ch, return all the alphabets upto i index of shortest.
            if other[i] != ch:
                return shortest[:i]
    return shortest 

