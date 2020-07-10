def intersection(arrays):
    # shorthanding the var, aslo it's a good practice to make a copy of the
    # data so that if the method breaks something you can eaily recover from
    # the var that was delaced originnally instead of having to reload the data
    # because sometimes it's not going to be possible to reload the data such
    # as streaming data from a sensor.
    a = arrays

    #print("INPUT:", a)

    # i think the quickest way to do this is count the len of the array then
    # use a freq distribution dict then check if there are any letters that
    # meet that legth
    result = []
    n = len(a)

    # flattening the list
    a = [y for x in a for y in x]
    seen = {}

    #print("FLATTENED LIST:", a)

    # make a count table
    for i in a:
        if str(i) not in seen.keys():
            seen[str(i)] = 1
        else:
            seen[str(i)] += 1

    print("COUNT TABLE VALUES OVER 1:",
          [f"k:{k} v:{v}" for k, v in seen.items() if v > 1])

    # I'm asserting that there isn't going to be a  case where there are
    # multiple dups per record. as in ther is never going to be a [1,1,1,9],
    #                                                             [1,2,3,4],
    #                                                             [1,8,7,9]
    # matrix this is a naive assumption but it should work for this application
    for k, v in seen.items():
        if (v == n) or (v > n):
            result.append(k)

    print("OUTPUT:", result)

    # being cheap and making sure that the return is sorted, might break it tho
    #result = sorted(result)

    return result


if __name__ == "__main__":
    # heres an interesting question why is it that I get the right answers
    # from the test here, but when I run the test it fails?
    arrays = [[1, 2, 3], [1, 4, 5, 3], [1, 6, 7, 3]]
    print(intersection(arrays))
