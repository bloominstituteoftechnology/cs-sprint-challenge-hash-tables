def finder(files, queries):
    """
    Params:
    -----
    files: list of file paths
    queries: list of files to search for

    Returns:
    -----
    results: list of file paths that contain the files in the
    queries

    """

    file_dict = dict()

    # I want to create a dictionary with the file name
    # being the key and the path being the value
    
    # get the name of the file by doing a right partition
    # on the file path then adding that file name to the 
    # dictionary
    for path in files:
        name = path.rpartition('/')[-1]
        if name not in file_dict:
            file_dict[name] = [path]
        else:
            file_dict[name].append(path)

    results = list()

    # look over the queries to see if any of the paths
    # lead to the files
    for query in queries:
        if query in file_dict:
            for path in file_dict[query]:
                results.append(path)

    return results


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
