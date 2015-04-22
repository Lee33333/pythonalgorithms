def swap(array, ind1, ind2):
	temp = array[ind1]
	array[ind1] = array[ind2]
	array[ind2] = temp

	return array

def min_Index(array, startIndex):
	min_val = array[startIndex]
	min_index = startIndex

	i = startIndex + 1
	for j in range(i, len(array)):
		if array[j] < min_val:
			min_val = array[j]
			min_index = j
	return min_index

def selection(array):
	for i in range(len(array)):
		small = min_Index(array, i)
		swap(array, i, small)
	print array

selection([3,2,1,88, -1,0])