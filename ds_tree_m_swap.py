class TreeNode(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def build_tree(nodes, node, i):
	if not node:
		return

	if (i*2)+1 < len(nodes):
		node.left = TreeNode(nodes[(i*2)+1])
		build_tree(nodes, node.left, (i*2)+1)
	if (i*2)+2 < len(nodes):
		node.right = TreeNode(nodes[(i*2)+2])
		build_tree(nodes, node.right, (i*2)+2)


def inorder(node):
	if not node or node.data == -1:
		return

	inorder(node.left)
	print(node.data)	
	inorder(node.right)


def swap_tree(root, swap):
	queue = [root]
	depth = 1
	
	while queue:
		node = queue.pop()
		left = node.left
		right = node.right
		depth += 1
		if depth == swap+1:
			node.right = left
			node.left = right
		else:
			queue.extend([left, right])


def k_swaps(nodes, swaps):
	root = TreeNode(1)
	build_tree(nodes, root, 0)
	for swap in swaps:
		swap_tree(root, swap)
		inorder(root)

n = int(input())
raw_nodes = [input().split() for i in range(n)]
nodes = []
for node in raw_nodes:
    nodes.extend([int(node[0]), int(node[1])])
t = int(input()) 
swaps = [int(input()) for i in range(t)]
k_swaps(nodes, swaps)
