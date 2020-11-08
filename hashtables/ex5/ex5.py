def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for path in files:
        file = path.split('/')[-1]

        if file in cache:
            cache[file].append(path)
        else:
            cache[file] = [path]

    result = []
    for a in queries:
        if a in cache:
            newResult = cache[a]
            for path in newResult:
                result.append(path)

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
