def has_negatives(a):
    map = {} 

    for n in a:
        if n != 0:
            an = abs(n)
            value = map.get(an)
            if value is None:
                map[an] = n
            else:
                map[an] = n+value

    # print(map)
    result = []

    for n in map.keys():      
        value = map.get(n)
        if value == 0:
            result.append(n)



    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
