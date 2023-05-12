'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]
    Example 2:

Example 2:
    Input: root = []
    Output: []
    
Example 3:
    Input: root = [1]
    Output: [1]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def _inorderTraversal(root, lst):
    # if root is None, return
    if root == None:
        return
    # call recursive function on left
    _inorderTraversal(root.left, lst)
    # append the root value to the lst
    lst.append(root.val)
    # call recursive function on right 
    _inorderTraversal(root.right, lst)
def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # Initialize lst and return lst
    lst = []
    _inorderTraversal(root, lst)
    return lst