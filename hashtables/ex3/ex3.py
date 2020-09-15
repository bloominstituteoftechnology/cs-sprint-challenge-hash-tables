# start with getting the value of all of the dictionaries first

def dict_value(value, dicts):
    for dict in dicts:
        if value not in dict:
            return False

    return True

# then we are going to iterate through each array and make a dictionary of unique values that we add to an array


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    unique_values_dictionary = []

    for array in arrays:
        unique_values = {}

        for value in array:
            unique_values[value] = True

        unique_values_dictionary.append(unique_values)

    #find last dict to check if any other dictionaries contain that same value

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
