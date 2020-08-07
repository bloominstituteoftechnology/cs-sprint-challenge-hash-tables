def intersection(arrays):
    """
    YOUR CODE HERE
    """
    length = len(arrays)
    nest = {y: {x: 0 for x in arrays[y]} for y in range(length)}
    result = {}
    for x in range(length-1):
        temp = nest[x]
        temp = dict(temp.items() & nest[x+1].items())
        result.update(temp.items())

    return list(result.keys())


if __name__ == "__main__":

    arrays = [[1,2,3],
              [1,4,5],
              [5,6,7]]

    print(intersection(arrays))
