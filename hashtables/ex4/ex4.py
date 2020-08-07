def has_negatives(a):
    pos_cache = {}
    neg_cache = {}
    result = []

    for n in a:
        if n > 0 and n not in pos_cache:
            pos_cache[n] = n
        elif n < 0 and n not in neg_cache:
            neg_cache[n] = n
    for n in neg_cache:
        k = abs(n)
        if k in pos_cache:
            result.append(pos_cache[k])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


# set cache for negative and positive values.
# if > 0 and not in positive cache add to pos cache
# elif < 0 and not in neg cache add to neg cache

# loop through neg cache
# set key to abs(value)
# if key in pos cache add to result
# return result
