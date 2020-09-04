# Your code here



def finder(files, queries):
    """
    goal: isolate filename from path, add to results if there is
    a matching query


    """
    # Your code here

    cache = {}
    stash = [] # might need this

    # loop through each path
    for path in files:
        # get the last 'word' from the path
        filename = path.split("/")[-1]

        # if filename in cache
        if filename in cache:
            # append that path to cache
            cache[filename].append(path)
        # else
        else:
            # do nothing? i guess
            cache[filename] = [path]

    # for each query
    for query in queries:
        # if the filename is in cache
        if query in cache:
            # append query to temp list
            stash.append(cache[query])
    
    # instantiate results
    result = []

    # for each list in temp list
    for j in stash:
        # read through each list
        for k in j:
            # append each item to the results list
            result.append(k)

    # spit back results
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
