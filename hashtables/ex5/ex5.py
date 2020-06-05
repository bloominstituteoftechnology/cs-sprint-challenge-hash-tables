# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    for path in files:
        file_item = path.split('/')[-1]
        
        if file_item in cache:
            cache[file_item].append(path)
        else:
            cache[file_item] = [path]

    result = []
    for query in queries:
        if query in cache:
            results = cache[query]
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
