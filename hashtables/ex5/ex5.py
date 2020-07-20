def finder(files, queries):
    """
    Given a list of full paths to files, and a list of filenames to query,
    report all the full paths that match that filename.
    """

    # Build a lookup table using a dictionary as follows:
    # Key: filename
    # Value: [path_1, path_2, etc.]
    lookup = {}
    for path in files:
        filename = path.split('/')[-1]
        if filename not in lookup:
            lookup[filename] = [path]
        else:
            lookup[filename].append(path)

    # Build a list of full paths matching each of a list of filenames.
    result = []
    for query in queries:
        if query in lookup:
            result += lookup[query]

    # Return all paths found.
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
