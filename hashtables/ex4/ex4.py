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

    for idx, num in enumerate(numbers):
        num_dict[idx] = num
        # print(num_dict)
        values = num_dict.values()
        # for num in numbers:
        print(values)
        if num > 0:
            print(num, "num")
            neg = numpy.negative(num)
            print(neg, "neg")

            if neg in values:
                print(num, "neg in num_dict")
                # result.append(num)

        # print(result)
        # return result


has_negatives(nums)

# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
