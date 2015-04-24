

def insertion_sort(array):
	#loop over the array, ignoring the 0th value
	for i in range(1, len(array)):
		#the value of the current index saved as the key
		current_val = array[i]
		position = i

		# while the index is greater than 0 and the number before it is greater than it
		while position > 0 and array[position -1] > current_val:
			#the value at this index becomes the value of the index before
			array[position] = array[position -1]
			#position is decremented
			position = position -1

		#array indexed by the decrimented position becomes the key of current val
		array[position] = current_val
	return array

print insertion_sort([3,4,1,0])







