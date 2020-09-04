def intersection(arrays):
    twoDimensionalArrray = arrays
    numberOfNestedArrays = len(twoDimensionalArrray)
    """
    YOUR CODE HERE
    """
    hashTable = {}
    solution = []
    
    for array in twoDimensionalArrray:
        for number in array:
            if number not in hashTable:
                hashTable[number] = 1
            else: #number in hashTable
                hashTable[number] +=1
            
    for (number, count) in hashTable.items():
        if count == numberOfNestedArrays:
            solution.append(number)

    return solution


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
