# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    paths_by_file = {}
    for path in files:
        components = path.split('/')
        filename = components[-1]
        if filename in paths_by_file:
            paths_by_file[filename].append(path)
        else:
            paths_by_file[filename] = [path]
    result = []
    for query in queries:
        if query in paths_by_file:
            result.extend(paths_by_file[query])
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
