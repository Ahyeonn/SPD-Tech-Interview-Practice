'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList( head):
    """
    :type head: ListNode
    :rtype: ListNode
    A -> B -> C -> D
    A <- B <- C <- D
    """
    # set prev to None
    prev = None
    # While head exists
    while head:
        # set cur_node to head
        cur_node = head 
        # set head to the head's next node
        head = cur_node.next
        # set cur_node's next to prev
        cur_node.next = prev
        # set prev to cur_node
        prev = cur_node # prev = Node A
    return prev
