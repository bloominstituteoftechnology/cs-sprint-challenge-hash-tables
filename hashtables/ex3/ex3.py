def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result=[]
    cache={}

    for array in arrays:
        for number in array:
            if number not in cache:
                cache[number] = 0
            else: # Number occurred previously
                if number not in result:
                    result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
