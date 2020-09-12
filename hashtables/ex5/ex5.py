# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Define working objects
    ret_lst  = []
    map_file = {}

    # Iterate through the list of file paths
    for pth in files:
        # Split the pth into path elements
        tmp_elm = pth.split("/")

        # Store the filename and path in our working map: filename => []path
        if tmp_elm[-1] not in map_file:
            # Filename not in map_file, create list value
            map_file[tmp_elm[-1]] = list([pth])
            continue

        # Processing a filename in multiple path locations
        map_file[tmp_elm[-1]].append(pth)

    # Iterate through the list of queries
    for qry in queries:
        # Is the filename found in the file map (as a key)?
        if qry not in map_file:
            # No. Skip this file query
            continue

        # Found filename, add to the return object (extend the return list)
        ret_lst.extend(map_file[qry])

    # Sort the return list object and return
    ret_lst.sort()
    return ret_lst


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
