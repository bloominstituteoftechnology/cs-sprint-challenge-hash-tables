import math

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    # like loopup_table app ex, using multiple caches
    pos_cache = {}
    neg_cache = {}
    #  zero will never show up

    # build up caches, we just want to look at keys later using abs mathy stuff
    for num in a:
        if num > 0:
            pos_cache[num] = 'present' 
        if num < 0:
            neg_cache[num] = 'present'


    # print(f' pos_cache {pos_cache}')             
    # print(f' neg_cache {neg_cache}')

    for kv in neg_cache.items(): 
        # print(f' key: {kv[0]} and abs is {abs(kv[0])}')  # key: -1 and abs is 1
        if abs(kv[0]) in pos_cache:    # absolute value to the rescue
            result.append(abs(kv[0]))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))





test_list = [-1,-2,1,2,3,4,-4]
print(has_negatives(test_list))      # [1,2,4]