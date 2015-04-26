#example of a fold function to work with a linked list

#function takes the head node, an accumulator variable, and another function
def fold(head, acc, f):
	#if there is a next node, call fold on it, after running acc through the other function
	if head.next:
		return fold(head.next, f(head.data, acc), f)
	#else just return the nodes data and the acc variable
	else:
		return f(head.data, acc)

#sending this function into fold would return the last item in linked list
def last(a,b):
	return a

#sending this function into fold would return the max data item in linked list
def max(a,b):
	if a > b:
		return a
	else:
		return b