# Make a hashtable that takes a num
# Create an object that takes every num inserted and makes a corresponding negative
# Check for nums
# Iterate through nums checking to see if corresponding negative exists
# If so, append to result


def has_negatives(a):

	negatives_by_number = {}

	for num in a:
		negatives_by_number[num] = -num # this is our negative number to check

	result = [] # array for nums with pos and neg

	for num in negatives_by_number.keys(): # 
		if num > 0 and negatives_by_number[num] in negatives_by_number:
			result.append(num)
    

	return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
