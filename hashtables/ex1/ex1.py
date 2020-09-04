def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    comps = {}
    for i in range(len(weights)):
      if (weights[i] in comps) and (weights[i] == comps[weights[i]][1]):
        return (i,comps[weights[i]][0])
      

      comps[weights[i]] = (i,limit-weights[i])

    sorted_comps = sorted(comps.items(), reverse=True, key=lambda x: x[1][0])

    for item in sorted_comps:
      if item[1][1] in comps:
        answer = (item[1][0],comps[item[1][1]][0])
        return answer
    
    return None
