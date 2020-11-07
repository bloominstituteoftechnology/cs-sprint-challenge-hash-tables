def intersection(arrays):
    ht = {} # initialize empty dict

    result = [] # intitalize empty list to add intersections

    for i in arrays:
        for elem in i: 
            if elem not in ht: 
                ht[elem] = 1 # amt of elem in ht 
            else: 
                ht[elem] += 1 # add intersection to ht
                if ht[elem] == len(arrays): # if intersection in every array
                    result.append(elem) # add intersection to result 
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
