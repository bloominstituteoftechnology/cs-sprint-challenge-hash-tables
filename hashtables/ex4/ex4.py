def has_negatives(integer_list):
    corresponding = {}
    result = []
    for integer in integer_list:
        if -integer in corresponding:
            result.append(abs(integer))
        else:
            corresponding[integer] = True
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
