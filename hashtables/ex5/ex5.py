def finder(files, queries):
    # Create an empty dict
    cache = {}

    # We'll loop through our files
    for path in files:
        # We'll use split to break up the input at the '/' separator and return a list of strings
        fileItems = path.split('/')[-1]
        # if the items are in cache
        if fileItems in cache:
            # we can append it to our dict
            cache[fileItems].append(path)
        else:
            cache[fileItems] = [path]

    result = []
    # We'll loop through our queries
    for query in queries:
        # if our query is in cache then we can continue and append our path to our result list
        if query in cache:
            results = cache[query]
            for path in results:
                result.append(path)
    # After our result list has been populated with the proper items, we can return it
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
