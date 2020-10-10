# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    #loop through queries
    for item in queries:
        #add queries to cache
        cache[item] = [item]

    #create list for results
    result = []

    #loop through files
    for item in files:
        #check if last part of file path is in cache
        if item.split("/")[-1] in cache:
            #if it is, append it to the list
            result.append(item)

    return result


    # cache = {} 

    # for item in files:
    #     name = item.split('/')[-1]
    #     if name in cache:
    #         cache[name].append(item)
    #     else:
    #         cache[name] = [item]
    
    # result = []

    # for item in queries:
    #     if item in cache:
    #         item_list = cache[item]
    #         for item in item_list:
    #             result.append(item)

    # return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
