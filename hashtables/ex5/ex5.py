# Your code here

# Given a list of file paths and a list of filenames to query
# return all the full file paths that match that filename


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    # The result will be in the form of a list
    result = []

    # Loop over all the paths in files and split off the filename
    for path in files:
        file_to_query = path.split("/")[-1]
        print(file_to_query)

        # if the file is already in the cache
        # append current path to that index
        if file_to_query in cache:
            cache[file_to_query].append(path)

        # otherwise add the file_to_query as the key and the path
        # as the value to the cache
        else:
            cache[file_to_query] = [path]

    # Loop over each file in the query list and check to see
    # if it is in the cache
    # If it is then add the path value to results
    for query in queries:
        if query in cache:
            results = cache[query]
            # for each path in results, append it to the result list
            for path in results:
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
