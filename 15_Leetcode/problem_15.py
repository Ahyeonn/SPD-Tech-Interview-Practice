'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # get size of the Linked List
    def get_size(self, head):
        size = 0
        root = head
        while root:
            size += 1
            root = root.next
        return size

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """ 

        # if one root and n = 1, return []
        if (self.get_size(head) == 1 and n == 1):
            return None
        
        # get size of the node
        len_node = self.get_size(head)
        cur_node = head
        prev_node = ListNode() # set prev_node to empty ListNode obj
        # traverse the head while it exists
        while cur_node:
            # set the prev_node to cur head
            prev_node = cur_node
            # if size of the node - 1 is equal to n, set node's next node as a next next node
            if len_node - 1 == n:
                cur_node.next = cur_node.next.next
                break
            # if n is equal to the size of the node, set head to the next node
            if n == len_node:
                head = cur_node.next
                break
            # traverse the node to the next node and decrement the size
            cur_node = cur_node.next
            len_node -= 1
        return head
