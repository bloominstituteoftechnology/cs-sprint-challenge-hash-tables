
def has_negatives(a):
   
    result = []
    num_count = {}

    for num in a:
        if abs(num) in num_count:
            num_count[abs(num)] += 1
        else:
            num_count[abs(num)] = 1

    for i in num_count:
        if num_count[i] > 1:
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))