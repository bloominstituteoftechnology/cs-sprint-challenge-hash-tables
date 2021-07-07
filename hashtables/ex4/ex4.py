def has_negatives(a):

    my_dict = {}
    result = []
    # define length and loop over list i
    for number in a:
        #always check if it's in the dictionary FIRST you moron!!!
        if abs(number) not in my_dict:
            my_dict[abs(number)] = number
        else:
            result.append(abs(number))
            print(result)
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
