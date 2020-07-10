def has_negatives(a):
    # define a hash table where the key is the values in the list and the value
    # for those keys are one
    cache = {k: 1 for k in a}

    # make a list of keys from the cache if the negitive is in the cache and if
    # the value is greater the 0
    result = [k for k, v in cache.items() if (k * -1) in cache and k > 0]

<<<<<<< HEAD
    return result
=======
# Think about storing the numbers in a dictionary and then looping through to see if the stored numbers have a negative counterpart - Dylan
# PS if you open a pull request from you branch to master I can leave reviews without having to leave a comment in your code like this

>>>>>>> d4a65d57db8d9a9466e22668b1fe7389a8c9bbe4


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
