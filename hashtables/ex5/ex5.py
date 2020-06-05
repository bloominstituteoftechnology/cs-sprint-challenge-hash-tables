# Your code here

import os
# from hashtable import HashTable

def finder(files, queries):
    """
    YOUR CODE HERE
    extract the base name and put it in hashtable
    import os
    print()
    print(os.path.basename('/users/system1/student1/homework-1.py'))
    print()
    """
    myHash = {}
    myHash2 = {}
    result = []
    for item in files:
        name = os.path.basename(item)
        if name not in myHash:
            myHash[name] = item
        else:
            myHash2[name] = item

    for query in queries:
        if query in myHash:
            result.append(myHash[query])
        if query in myHash2:
            result.append(myHash2[query])

    return result


if __name__ == "__main__":
    # files = [
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz'
    # ]
    # queries = [
    #     "foo",
    #     "qux",
    #     "baz"
    # ]
    # print(finder(files, queries))
    files = []

    for i in range(500000):
        files.append(f"/dir{i}/file{i}")

    for i in range(500000):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    queries = []

    for i in range(1000000):
        queries.append(f"nofile{i}")

    queries += [
        "file3490",
        "file256",
        "file999999",
        "file8192"
    ]

    print(finder(files, queries))
    # print(result.sort())