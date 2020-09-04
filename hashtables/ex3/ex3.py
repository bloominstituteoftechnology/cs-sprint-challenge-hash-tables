# get the value of all dictionaries first

def dict_value(value, dicts):
    for dict in dicts:
        if value not in dict:
            return False

    return True

#Iterate through each array and make a dictionary of unique values
#add each of those to an array
# I plan on checking the last dict and checking if any other dictionaries contain that value
# append that 

def intersection(arrays):
    
    unique_values_dictionary = []

    for array in arrays:
        uninque_values = {}

        for value in array:
            uninque_values[value] = True

        unique_values_dictionary.append(uninque_values)

    # Find last dict
    last_dict = unique_values_dictionary[-1]
    result = []

    for value in last_dict:
        if dict_value(value, unique_values_dictionary[:-1]):
            result.append(value)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
