def has_negatives(a):
    result = []
    my_dict = {}

    for num in a:
        my_dict[num] = num

        if num != 0 and - num in my_dict:
            result.append(abs(num))

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
