def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Instantiate a cache dict 'occurences'
    occurrences = dict()
    
    # Loop over every list in arrays
    for i in range(len(arrays)):
        # Loop ober each number
        for num in arrays[i]:
            # Check to see if num has 'occurred' yet
            if num not in occurrences:
                occurrences[num] = 1
            
            # If it has then add an occurrence
            else:
                occurrences[num] +=1
    
    # Instantiate result
    result = []

    # If the number has occurred in every list in arrays then
    # we add it to result
    l = len(arrays)
    result = result + [k for k,v in occurrences.items() if v == l]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
