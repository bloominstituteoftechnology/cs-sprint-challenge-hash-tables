from collections import Counter

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # first convert lists into dictionary
    # print(arrays)
    # result = {}
    count = 0
    lst = []
    for i in arrays:
        # print(i)
        if isinstance(i, list):
            ar1 = Counter(i)
            count += 1
            lst.append(ar1)

    # print(lst)
    result = Counter()

    answer = []
    for i in lst:
        result += i

    for (key, value) in result.items():
        # print(key, value)
        if value == count:
            answer.append(key)
    # for i in result:
    # print(i)

    return answer


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
