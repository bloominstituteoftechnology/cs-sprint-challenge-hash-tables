def value_in_all_dicts(value, dicts):
        for dict in dicts:
            if value not in dict:
                return False
        return True

def intersection(arrays):
    unique_value_dicts = []

    for array in arrays:
        unique_values = {}
        for value in array:
            unique_values[value] = True
        unique_value_dicts.append(unique_values)
    
    last_dict = unique_value_dicts[-1]
    result = []

    for value in last_dict:
        if value_in_all_dicts(value, unique_value_dicts[:-1]):
            result.append(value)
    return result


if __name__ == "__main__":
    arrays = []
    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])
    print(intersection(arrays))