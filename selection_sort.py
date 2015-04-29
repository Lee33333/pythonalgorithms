# go through array until n  or n -1
# find the largest number, remember its index
# at end of the array, switch the last number and the largest number

def selection_sort(array):
	for j in range(len(array) -1, 0, -1):
		max_index = 0
		for i in range(j):
			if array[i] > array[max_index]:
				max_index = i
		if array[max_index] > array[j]:
			temp = array[max_index]
			array[max_index] = array[j]
			array[j] = temp

	return array



print selection_sort([3,2,1,88, -1,0, 202, -15])









# def swap(array, ind1, ind2):
# 	temp = array[ind1]
# 	array[ind1] = array[ind2]
# 	array[ind2] = temp

# 	return array

# def min_Index(array, startIndex):
# 	min_val = array[startIndex]
# 	min_index = startIndex

# 	i = startIndex + 1
# 	for j in range(i, len(array)):
# 		if array[j] < min_val:
# 			min_val = array[j]
# 			min_index = j
# 	return min_index

# def selection(array):
# 	for i in range(len(array)):
# 		small = min_Index(array, i)
# 		swap(array, i, small)
# 	print array
