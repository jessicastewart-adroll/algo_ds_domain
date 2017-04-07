
class TreeNode(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def print_inorder(node):
	if not node or node.data == -1:
		return

	print_inorder(node.left)
	print(node.data)	
	print_inorder(node.right)

def build_tree(nodes, parent, depth):
	if depth > len(nodes)-1:
		return

	parent.left = TreeNode(nodes[depth][0])	 
	parent.right = TreeNode(nodes[depth][1])
	build_tree(nodes, parent.left, depth+1)	
	build_tree(nodes, parent.right, depth+2)	 

nodes_one = [[2, 3], [-1, -1], [-1, -1]]
swaps_one = [1, 1]
nodes_two = [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
swaps_two = [2, 3]
nodes_three = [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]]
swaps_three = [2, 4]

parent = TreeNode(1)
# build_tree(nodes_one, parent=parent, depth=0)
# build_tree(nodes_two, parent=parent, depth=0)
build_tree(nodes_three, parent=parent, depth=0)
print_inorder(parent)
