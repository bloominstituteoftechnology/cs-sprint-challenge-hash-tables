def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    uni_dict = []

    for n in arrays:
        uni_val = {}

        for val in n:
            uni_val[val] = True

        uni_dict.append(uni_val)

    last_dict = uni_dict[-1]
    result = []

    for val in last_dict:
        if all_dict_val(val, uni_dict[:-1]):
            result.append(val)

    return result

def all_dict_val(val, dicts):
        for n in dicts:
            if val not in n:
                return False

        return True

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
