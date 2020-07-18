def get_indices_of_item_weights(weights, length, limit):
	"""
	YOUR CODE HERE
	# Loop through the lendth
	# Then loop through each of the weights
	# Make sure your not adding the same index with itself
	# if the 2 weights equal the limit,
	# check to see which index is greater than each other and return it
	"""
	# Your code here
	for i in range(0, length):
		for weight in weights:
			if weights.index(weight) != i:
				if weight + weights[i] == limit:
					if weights.index(weight) > i:
						return [weights.index(weight), i]
					else:
						return [i, weights.index(weight)]

	return None
