# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # set up cache
    cache = {}
    # results list
    result = []
    # making a cache of paths
    for path in files:
        # the file is the last name after last / divider
        file_item = path.split('/')[-1]
        # if item is in cache
        if file_item in cache:
            # append path to locations that are known
            cache[file_item].append(path)
        else:
            # create a list if item is not in cache
            cache[file_item] = [path]

    #  loop to check queries
    for q in queries:
        # if query is in cache
        if q in cache:
            # set results to cache
            results = cache[q]
            # return a list of paths
            # return lists into one list
            for path in results:
                # append list of path
                result.append(path)
    else:
        # if not then pass
        pass

    return result


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
