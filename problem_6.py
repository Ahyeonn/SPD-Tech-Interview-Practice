'''
Given two sorted linked lists, merge them so that the resulting linked list is also sorted.

<Example>
input_node_1 = Node(4(Node(8, Node(15, Node 19))))
input_node_2 = Node(7(Node(9, Node(10, Node 16))))

result = Node(4(Node7, Node(8, Node(9, Node(10, Node(15, Node(16, Node(19))))))))
'''
class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

def merge_linked_list(input_node_1, input_node_2):
  head = Node(None)
  cur_node = head # pointing at same memory location

  while input_node_1 and input_node_2:
    if input_node_1.val < input_node_2.val: # Node 1 < Node2
      cur_node.next = input_node_1
      input_node_1 = input_node_1.next
    else:
      cur_node.next = input_node_2
      input_node_2 = input_node_2.next
    cur_node = cur_node.next  

# Iterate and check 
  if input_node_1 != None:
    cur_node.next = input_node_1
    # new_nodes = root_node_1.val
  if input_node_2 != None:
    cur_node.next = input_node_2
  return head.next # points to Node 1 and head in here is Dummy head

def print_out_linked_list(root):
  while root:
    print(root.val)
    root = root.next
  return

input_node_1 = Node(4, Node(8, Node(15, Node(19))))

input_node_2 = Node(7, Node(9, Node(10, Node(16))))

print_out_linked_list(merge_linked_list(input_node_1, input_node_2))
