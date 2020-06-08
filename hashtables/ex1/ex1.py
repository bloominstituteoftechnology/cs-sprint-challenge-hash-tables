from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for index, item in enumerate(weights):
        hash_table_insert(ht, item, index)

    for index, item in enumerate(weights):
        goal = limit - item
        lookup = hash_table_retrieve(ht, goal)
        if lookup is not None:
            return max(index, lookup), min(index, lookup)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
