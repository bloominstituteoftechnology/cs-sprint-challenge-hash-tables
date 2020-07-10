def has_negatives(a):

    list_of_integers = a

    dict_of_integers = {}

    for integer in list_of_integers:
        if integer > 0:
            dict_of_integers[integer] = 'positive'

    for integer in list_of_integers:
        if integer < 0 and -integer in dict_of_integers:
            dict_of_integers[-integer] = 'both'

    # print( dict_of_integers )

    ret_list = [k for (k, v) in dict_of_integers.items() if v == 'both']

    result = ret_list

    # print(ret_list)

    # return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

    print(has_negatives([ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]))