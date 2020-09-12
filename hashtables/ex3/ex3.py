from typing import List
def intersection(arrays: List) -> List:
    """
    YOUR CODE HERE
    """
    result = {}
    intersects = {}
    for ii in arrays:
        for num in ii:
            if num not in intersects:
                intersects[num] = 1
            else:
                intersects[num] += 1

    return [res for res, val in intersects.items() if val == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
