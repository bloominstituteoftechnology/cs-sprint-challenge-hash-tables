def finder(files, queries):
    """
    YOUR CODE HERE
    """
    q = {}
    # add all queries to dict
    for query in queries:
        q[query] = query
    matches = []
    for file in files:
        # for each part of the path (split of the delimiter '/')
        for f in file.split("/")[1:]:
            # if matches a query
            if f in q:
                # append matches
                matches.append(file)
    return matches


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

    # you would want to check each path item to see
    # if it matches any of our queries, which we 
    # have in our dict, if they do we could add the 
    # full path to a list (so don't mess up the path permanently)