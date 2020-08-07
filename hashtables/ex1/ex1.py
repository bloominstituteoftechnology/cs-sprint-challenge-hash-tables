from hashtable import HashTable

hash_table = HashTable()
def get_indices_of_item_weights(weights, length, limit):
    # Your code here

    # hash table solution

    for index in range(length):
        weight = str(weights[index])
        hash_table.put(weight, index)

    for index in range(length):
        if index is None:
            return None
        else:
            remainder = limit - weights[index]
            if hash_table.get(str(remainder)):
                return [hash_table.get(str(remainder)), index]

        

    # cache solution

    # cache = {}

    # for index in range(length):
    #     weight = weights[index]
    #     cache[weight] = index
    # for index in range(length):
    #     remainder = limit - weights[index]
    #     if remainder in cache:
    #         return (cache[remainder], index)

get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)
