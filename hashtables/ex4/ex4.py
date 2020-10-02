def has_negatives(a):
    # Your code here

    num_dict = {} # capture all numbers here, positive & negative
    output = [] # if positive number appears in num_dict, check if also has negative, if so append positve to output

    for num in a:
        if num not in num_dict: # if not in dict yet
            num_dict[num] = 0 # put in dict w/no value to start
    
    # for all the nums in the dict, look for negative pair of positive nums
    for nums in num_dict.items():
        if nums[0] > 0: # if a positive number
            if (nums[0] * -1) in num_dict: # check to see if negtive number also exists
                output.append(nums[0]) # if so, append positve number to dict
    # print(output)
    return output

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
