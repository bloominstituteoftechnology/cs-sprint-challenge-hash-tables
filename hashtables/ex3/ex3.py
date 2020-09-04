class HashTable:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.hash_map = [[] for _ in range(0, self.capacity)]
        print(self.hash_map)


def hashing_function(hash_table, key):
    hashed_key = hash(key) % hash_table.capacity
    return hashed_key


def intersection(arrays):
    """
    YOUR CODE HERE
    """

    # Your code here
    result = [value for value in lst1 if value in lst2]
    return result

h = HashTable()
print(h)
# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
