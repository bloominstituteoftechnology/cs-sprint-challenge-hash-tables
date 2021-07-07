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