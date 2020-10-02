# Your code here
import re


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for query in queries:
        cache[query] = []
    for file in files:
        broken = file.rsplit('/', 1)
        broken = broken[-1]
        if broken in cache:
            cache[broken].append(file)
    for query in queries:
        if query in cache:
            for item in cache[query]:

                result.append(item)
      
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/usr/foo'

    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
