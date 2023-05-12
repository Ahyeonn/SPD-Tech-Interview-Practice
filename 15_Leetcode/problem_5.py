'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false

Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def _isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    # Edge cases: if p is None but q exists, return False
    if p is not None and q is None:
        return False
    # if p exists, but q is None, return False
    elif p is None and q is not None:
        return False
    # if p and q are both None, return True
    elif p is None and q is None:
        return True
    # if p value and q value is unequal, return False
    elif p.val != q.val:
        return False
    # call recursive function on both of p & q's left and also p & q's right
    return _isSameTree(p.left,q.left) and _isSameTree(p.right, q.right)        

# call recursion function
def isSameTree(p, q):
    return _isSameTree(p,q)