def has_negatives(a):

    number_dict = dict()
    has_neg = list()

    for number in a:
        if (number * -1) in number_dict:
            has_neg.append(abs(number))
        number_dict[number] = True
    
    return list(set(has_neg))


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
