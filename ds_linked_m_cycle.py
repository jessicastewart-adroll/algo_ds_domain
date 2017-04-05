"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
def has_cycle(head):
	if not head:
		return False
	else:
		seen = set()
		node = head
		while node.next:
			if node.data in seen:
				return True
			seen.add(node.data)
			node = node.next

		return False
