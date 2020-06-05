def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    list_integers = {}
    result = []
    for x in arrays:
        for y in x:
            if y not in list_integers:
                list_integers[y] = 0
            else:
                result.append(y) 
    result= list(dict.fromkeys(result))

    return result
"""
line 7: if array in dictionary
line 8: x is single list
line 9: j is item in the list x
line 10: if j is not in dictionary 
line 11: j = key and 0 has value
line 12: append j to the resulting list  
line 13: removes duplicates out of the list and creates a new list 
"""


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
