# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    #set cache
    cache = {}
    # splitting paths from / to grab filename
    for path in files:
        file_item = path.split('/')[-1]
        # if already in cache append path to cache
        if file_item in cache:
            cache[file_item].append(path)
        # otherwise set path
        else:
            cache[file_item] = [path]
    result = []
    # for each file name in the query check cache in results
    for query in queries:
        if query in cache:
            results = cache[query]
            for path in results:
                result.append(path)
    # Your code here

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
