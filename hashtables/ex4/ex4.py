def has_negatives(a):
    # for this question im going to take a quick and dirty approch
    # if the number is above 0 then check if n* -1 is in array, if true apppend
    # to the output list, if false pass to next element

    output = []
    for i in a:
        if i > 0:
            if (i * -1) in a:
                output.append(i)
            else:
                pass
        else:
            pass
    return output


# this solution is O(n^2) because we are technically indexing the list twice,
# once when we iterate through the list, and again when we check if -i is in a
# since the second loop is within the first its get the exponent treatment
# no this might not actually be a O(n^2) because I don't know what the
# data structure is for the (n is in array) im assuming that opperation is O(n)

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

# AFTER THE FACT NOTE:
# this takes literally forever to run so def a O(n^2)
# further improvments would be use a lookup table and see if there are cache
# optimizations that can be done to improve runtime
# also using multiple threads would be nice, bi-passing python's gli with the
# multiprocessing library is an option also
