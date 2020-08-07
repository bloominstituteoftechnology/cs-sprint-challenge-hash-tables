# from hashtable import HashTable

def intersection(arrays):
    # Your code here
    nums = {}
    intersections = []
    for arr in arrays:
        for i in arr:
            if i not in nums:
                nums[i] = [i]
            else:
                nums[i].append(i)

    for i in nums:
        if len(nums[i]) >= len(arrays):
            intersections.append(i)
    # print(f'NUMS: {nums}')
    # print(f'INTERSECTIONS: {intersections}')

    return intersections
            


# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))

intersection([[1, 2, 3, 4, 5],[12, 7, 2, 9, 1],[99, 2, 7, 1,]])
