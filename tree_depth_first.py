#function takes stack containing tree root node
def depth_first(stack):
	#if the stack is not empty
	if stack:
		#pop off first item in the stack
		x = stack.pop()
		#print it
		print x
		#if it has a right child, push it onto the stack
		if x.right:
			stack.push(x.right)
		#if it has a left child, push it onto the stack
		if x.left:
			stack.push(x.left)
		#call function on the stack recursively, which means all the lefts will be popped first
		depth_first(stack)