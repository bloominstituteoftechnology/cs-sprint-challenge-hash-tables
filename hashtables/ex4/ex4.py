def has_negatives(a):
    #sort the array
    sorted_array = sorted(a)
    
    # put array in a dictionary
    cache = {}
    for i in range(len(a)):
        cache[a[i]] = i
    
    result = []
    # loop through negative numbers and see if it's in dictionary
    num = 0
    while sorted_array[num] < 0:
        if (sorted_array[num] * -1) in cache:
            result.append(sorted_array[num] * -1)
        num += 1    

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
