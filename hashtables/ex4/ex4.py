import pprint
import numpy

nums = [-1, -2, 1, 2, 3, 4, -4]


def has_negatives(numbers):
    """
    YOUR CODE HERE
    """
    # Your code here

    # if we store everything in a dict
    # query dict to find corresponding negative number
    # append to array

    num_dict = {}
    result = []

    for num in numbers:

        # absol_num = abs(num)

        # num_dict[absol_num] = num

        if num_dict.get(abs(num)):

            if (num_dict.get(abs(num)) + num) == 0:
                result.append(abs(num))
        else:
            num_dict[abs(num)] = num

    print(result)
    return result


has_negatives(nums)

# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
