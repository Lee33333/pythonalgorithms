
def bubble_sort(array):
	# for every item starting at the end, moving backwards to zero
	# takes care of the n-1 length of the algorithm
	for j in range(len(array)-1, 0, -1):
		# from zero to our current length
		for i in range(j):
				#if the next item is bigger, swap them
				if array[i] > array[i + 1]:
					temp = array[i]
					array[i] = array[i + 1]
					array[i + 1] = temp
	return array

print bubble_sort([4, 6, 5, 1, 0, 7, 8, 3])

