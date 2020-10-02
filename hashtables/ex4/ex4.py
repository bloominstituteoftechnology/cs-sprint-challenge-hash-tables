def has_negatives(a):
    cache = {}
    result = []

    for i in a:
        if i != 0:
            cache[i] = 1
            if -i in cache:
                result.append(abs(i))

     return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
