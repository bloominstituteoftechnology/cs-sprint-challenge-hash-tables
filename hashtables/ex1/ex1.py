class HashEntry:
    def __init__(self, weight, index):
        self.weight = weight
        self.index = index
        self.next = None

    def __repr__(self):
        return f"(W: {self.weight}, i:{self.index}) {self.next}"


def get_indices_of_item_weights(weights, length, limit):
    d = {}
    res = ()
    if length <= 1:
        return None
    for i in range(len(weights)):
        if weights[i] not in d:
            d[weights[i]] = HashEntry(weights[i], i)
        else:
            current = d[weights[i]]
            while current.next is not None:
                current = current.next
            current.next = HashEntry(weights[i], i)
    for i in range(len(weights)):
        val = limit - weights[i]
        if val in d:
            res = (i, d[val].index)
    res = tuple(sorted(res, reverse=True))
    return res
