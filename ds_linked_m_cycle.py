class Node(object):
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next = next_node

def has_cycle(head):
	if not head:
		print('0')
	else:
		seen = set()
		node = head
		while node.next:
			if node.data in seen:
				print('1')
				return
			seen.add(node.data)
			node = node.next

		print('0')

head = None
has_cycle(head) # 0

head = Node(1)
node2 = Node(2)
node3 = Node(3)
head.next=node2
node2.next=node3
node3.next=node2
has_cycle(head) # 1

node3.next=None
has_cycle(head) # 0
