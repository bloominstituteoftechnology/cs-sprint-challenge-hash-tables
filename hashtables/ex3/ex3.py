def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #iterate through the first array hashing each item
    #iterate through second:
        #if item in second in first then append to intersections
    #continue through lists checking if items in intersections is in current
    chill = None
    for i in range(len(arrays)):
        arrays[i] = set(arrays[i])
        if i == 0:
            chill = arrays[i]
        else:
            temp = chill.intersection(arrays[i])
            chill = temp
    result = list(chill)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
