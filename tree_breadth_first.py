#function accepts a stack containing tree root
def breadth_first(queue):
	#if queue not empty
	if queue:
		#take item off end of queue an print it
		x = queue.pop()
		print x
		#if it has a right child, add it to queue
		if x.right:
			queue.push(x.right)
		#if it has a left child, add it to queue
		if x.left:
			queue.push(x.left)
		#call function on queue again
		breadth_first(queue)
