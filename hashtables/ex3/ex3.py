def intersection(arrays):
    # Your code here

    count = {} # list of all integers w/their count

    # iteratve over the array of arrays
    for i in arrays:
        for j in i: # iterate through each array
            if j not in count: # if the int is not in the count dict yet
                count[j] = 0
            count[j] += 1 # then add it
    
    output = [] # empty array to hold intersections, i.e. ints that appear the number of times equal to lenght of array
    countof_arrays = len(arrays) # get a count of how many arrays were passed in

    # need to find if a given int's count is equal to the lenght of the arrays (so if 3 arrays & count is 3, it appears in each)
    # if so, append to the output array
    for i in count.items():
        if i[1] == countof_arrays:
            output.append(i[0])

    # print(output)
    return output


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
