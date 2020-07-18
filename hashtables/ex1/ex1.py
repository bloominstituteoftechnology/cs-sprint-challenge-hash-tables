def get_indices_of_item_weights(weights, length, limit):
	"""
	YOUR CODE HERE
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
