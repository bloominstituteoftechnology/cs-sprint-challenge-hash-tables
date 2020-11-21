def get_indices_of_item_weights(weights, length, limit):

    if length <= 1:
        return None

    package = {}

    for item in range(length):
        weight = weights[item]

        if weight in package:
            value = package[weight]
            return (item, value)
        
        differece = limit - weight
        package[differece] = item

    return None
