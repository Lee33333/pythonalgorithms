def rev_ll(node):

	# set up two pointer variables
	last= None
	current = node

	# while there is a next node:
	while current.next:
		#set up temp to hold place for next node in line
		nxt = current.next
		#connect the current node to the last one
		current.next = last
		#reset the last node to the current
		last = current
		#reset the current to the next
		current = nxt

	#connect the last node to the second to last and return it
	current.next = last
	return current