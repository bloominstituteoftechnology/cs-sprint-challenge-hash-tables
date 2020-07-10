def intersection(lists):
    """
    YOUR CODE HERE
    """
    length = len(lists)
    my_dict = {}
    for array in lists:
      for num in array:
        if num not in my_dict:
          my_dict[num] = 1
        else:
          my_dict[num] += 1

    ans = []

    for item in list(my_dict.items()):
      if item[1] == length:
        ans.append(item[0])

    return ans


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
