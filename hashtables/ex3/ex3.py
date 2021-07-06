def intersection(arrays):
    """
    YOUR CODE HERE
    """
    dict = {} 
    result = [] 

    for i in arrays:
        for e in i: 
            if e not in dict: 
                dict[e] = 1 
            else: 
                dict[e] += 1 
                if dict[e] == len(arrays): 
                    result.append(e)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
