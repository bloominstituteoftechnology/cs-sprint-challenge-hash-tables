def has_negatives(a):
    result=[]
    cache={}

    for number in a:
    	cache[number] = 0
    for number in a:
    	# Turn negative to positive
    	temp = number * -1
    	# If theres a positive version, add to results
    	if temp in cache and temp < 0:
    		result.append(number)


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
