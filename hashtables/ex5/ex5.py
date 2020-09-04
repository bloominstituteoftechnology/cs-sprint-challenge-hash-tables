# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # set up dict
    my_dict = {}
    # results list
    result = []
    # making a dict of paths
    for path in files:
        # the file is the last name after last / divider
        file_item = path.split('/')[-1]
        # if item is in my_dict
        if file_item in my_dict:
            # append path to locations that are known
            my_dict[file_item].append(path)
        else:
            # create a list if item is not in my_dict
            my_dict[file_item] = [path]

    #  loop to check queries
    for q in queries:
        # if query is in my_dict
        if q in my_dict:
            # set results to my_dict
            results = my_dict[q]
            # return a list of paths
            # return lists into one list
            for path in results:
                # append list of path
                result.append(path)
    else:
        # if not then pass
        pass

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
