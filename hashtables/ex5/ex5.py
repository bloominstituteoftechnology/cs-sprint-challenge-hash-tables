# Your code here

import os
import glob


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    # path = '.'
    # result = []

    # # The list of items
    # files = os.listdir(path)

    # # Loop to print each filename separately
    # for queries in files:
    #     result.append(queries)
    files_ = files
    hash_table = {}
    end = []
    result = []

    for file in files_:
        path = ''
        while file[-1] != '/':
            # add file[-1]to paths value 
            path += file[-1]
            # reassign  
            file = file[:-1]
        # assign paths from file -->  start at the end then append(path )
        path = path[::-1]
        end.append(path)

    files_list_range = range(len(files_))
    for i in files_list_range:
        if end[i] not in hash_table:
            hash_table[end[i]] = []
        hash_table[end[i]].append(files_[i])

    for q in queries:
        if q in hash_table:
            r = hash_table.get(q)
            for a in r:
                result.append(a)

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
