def finder(paths, queries):
    
    q = {}

    # add all queries to dict
    for query in queries:

        q[query] = query

    matches = []

    for path in paths:

        # for each part of the path (split of the delimiter '/')
        for f in path.split("/")[1:]:

            # if matches a query
            if f in q:

                # append matches
                matches.append(path)

    return matches


if __name__ == "__main__":
    paths = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(paths, queries))

        # Given a list of full paths to files, and a list of filenames to query,
    # report all the full paths that match that filename.

    
        
    # you would want to check each path item to see if it matches any of our queries, which we 
    # have in our dict, if they do we could add the full path to a list (so don't mess up the path permanently)


