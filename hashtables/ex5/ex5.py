# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """

    cache = {}
    # We'll create a cache of item:paths 
    for path in files:
        # the file is the last item after last '/'
        file_item = path.split('/')[-1]
        
        # if that item is in cache, append path to known locations
        if file_item in cache:
            cache[file_item].append(path)
        # if that item is not in cache, create a list with path
        else:
            cache[file_item] = [path]

    result = []
    # check to see if each query is a key in our cache
    for query in queries:
        if query in cache:
            results = cache[query]
            # because we are returning a list of paths, we collapse list of lists into one list
            for path in results:
                result.append(path)
    else:
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
