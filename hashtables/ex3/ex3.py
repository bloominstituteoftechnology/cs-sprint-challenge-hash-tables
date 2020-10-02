def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    #create a cache dictionary
    #create a result list where I will store the values that intersect (that are the same) between lists
    cache = {}
    result = []
    
    #checking to see how many lists I am working with and storing the lists in list_count
    list_count = len(arrays)
    print(list_count)

    for number_list in arrays:
        for number in number_list:
            if number in cache:
                # if the number is cache, incremenet the key count
                cache[number] +=1
            else:
                #if the number is not in cache, add a key count of 1
                cache[number] = 1
            #if the number in cache is the same as any numbers inside the list_count
            if cache[number] == list_count:
                result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
