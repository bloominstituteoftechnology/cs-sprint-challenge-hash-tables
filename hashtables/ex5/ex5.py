# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for file in files:
        file = file.split("/")
        if file[-1] not in cache:
            cache[file[-1]] = []
        cache[file[-1]].append("/".join(file[:-1]))
    for query in queries:
        if query in cache:
            for file in cache[query]:
                result.append(file + "/" + query)
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
