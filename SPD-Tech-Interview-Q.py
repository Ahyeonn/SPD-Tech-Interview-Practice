class Solution(object):
    def isValid(self, s):
        """
        <Question>
        The input string s contains "(", ")", "{", "}", "[", "]". Determine if the input string is valid. 
        An Input string is valid if:
            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
            Every close bracket has a corresponding open bracket of the same type.

        <Example>
        Input: s = "()" -> True
        Input: s = "()[]{}" -> True
        Input: s = "(]" -> False

        <Pseudocode>
        1. Set a dictionary for string s to find the matching characters. 
        2. Iterate string s and check if it is a properly ordered character. 
        3. if they do not match, return False. Else grab the next iterated value
        
        :type s: str
        :rtype: bool
        """
        Map = {")": "(", "]": "[", "}": "{"}
        stack = [] # (

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack

        