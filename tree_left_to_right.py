		traverse(node.left)
		traverse(node.right)
	#if node has a left child, call recursively on it
	#if node has a right child, call recursively on it
	#print the node itself
	if node.left
	if node.right
	print node.data
#function takes the root node of a binary tree
def traverse(node):