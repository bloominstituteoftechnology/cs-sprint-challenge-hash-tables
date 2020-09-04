def has_negatives(a):
    array = a
    """
    YOUR CODE HERE
    """
    hashTable = {}
    solution = []
    
    for number in array:
        number = abs(number)
        if hashTable.get(number) is None:
            hashTable[number] = "Added this number to hashtable"
        else: #already exists
            solution.append(number)
            
    return solution


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
