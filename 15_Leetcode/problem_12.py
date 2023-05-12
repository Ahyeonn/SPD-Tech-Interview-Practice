'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false
'''

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # Create dic to pair the key and value as opposite parentheses
    Map = {")": "(", "]": "[", "}": "{"}
    stack = []

    # Iterate through s
    for c in s:
        # If iterated value is not in the Map then add it to the stack
        if c not in Map:
            stack.append(c)
            continue
        # If stack is empty or the last element that is added to the stack is not equal to the value pair, return False
        if not stack or stack[-1] != Map[c]:
            return False
        # Every iteration, remove the added parentheses from the stack
        stack.pop()

    return not stack