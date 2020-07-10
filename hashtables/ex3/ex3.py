def intersection(arrays):
    
    lists = arrays
    list_count = len(lists)
    
    tally = {}
    
    for i in lists[0]:
        tally[i] = 1
        
    for other_list in lists[1:]:
        
        for el in other_list:
            if el in tally:
                tally[el] += 1
                
    final_list = [k for (k,v) in tally.items() if v == list_count]
    result = final_list

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
