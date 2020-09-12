# Your code here



def finder(files, queries):
    """
    given a list of filepaths, and a list of query filenames, returns those filepaths
    whose filenames are in the query.
    """
    
    # init dict
    d = {}

    # add all the queries to the dict
    for query in queries:
        d[query] = query

    # loop over the files, and check if the filename is in queries
    result = []

    for filename in files:
        if filename.split('/')[-1] in d:
            result.append(filename)

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
