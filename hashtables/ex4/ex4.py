from typing import List


def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}

    for i in a:
        cache[i] = -i

    # return(cache)
    negatives = {k:v for k, v in cache.items() if k < 0}

    return(list(set(negatives.values()).intersection(set(a))))

 

  

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
