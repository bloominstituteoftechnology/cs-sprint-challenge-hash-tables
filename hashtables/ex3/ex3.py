def intersection(arrays):
    """
    YOUR CODE HERE
    Given a list with x amount of lists containing nums
    Find the nums that are all the lists
    Up to 10 lists inside 
    Each list cna have up to ALOT of nums

    Find all the nums that exist in all given lists
    Return results = array

    loop through main list to get all secondary list
    loop through secondary list to get all elements
    if num is not in hashtable add it to table 
    If it is in table then its duplicate
    add to results
    """
    # Your code here
    table = {}   #hashtable
    result = [] #return array

    for a in arrays:
        for num in a:
            if num not in table:
                table[num] = None

            if num not in result:
                result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
