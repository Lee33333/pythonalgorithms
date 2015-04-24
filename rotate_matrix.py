
# '''
# Turn Matrix
# Input: 4x3 matrix of integers
# Output: Rotate the matrix by 90 degrees and return rotated matrix
# Example:
# [[1 2 3 10],
# [4 5 6 11],
# [7 8 9 12]]
# Switch to:
# 7 4 1
# 8 5 2
# 9 6 3
# 12 11 10
# '''

def turn(matrix):
	#generate new matrix
	new_matrix = []
	# get the original height, in this case 3
	height = len(matrix)
	# get the original length, in this case 4
	length = len(matrix[0])
	#four times, we want to
	for i in range(length):
		j = height
		my_array = []
		#print three numbers, ie from j = 3 to 0
		while j > 0:
			#j here is adjusted to be 2 from 3, because its an iterator
			j = j-1
			my_array.append(matrix[j][i])
		new_matrix.append(my_array)
	return new_matrix

print turn([[1, 2, 3, 10],[4, 5, 6, 11],[7, 8, 9, 12]])



