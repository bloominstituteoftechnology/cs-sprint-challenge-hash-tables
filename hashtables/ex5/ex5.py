import ntpath
import itertools


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    names = {}
    file_temp = files
    file_temp[:] = map(lambda x: (x, ntpath.basename(x)), files)
    names.update([file for file in file_temp])

    result = []
    for item in queries:
        if item in names.values():
            result.append(list(names.keys())[list(names.values()).index(item)])

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

    result = finder(files, queries)
    print(result)