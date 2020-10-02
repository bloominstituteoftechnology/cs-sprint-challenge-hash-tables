# Your code here
import re


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    answer = []
    for query in queries:
        cache[query] = []
    for file in files:
        f = (file + '.')[:-1]
        broken = file.rsplit('/', 1)
        broken = broken[-1]
        if broken in cache:
            #start = cache[broken[-1]]
            cache[broken] += f
    for query in queries:
        if query in cache:
            result.append(cache[query])
    for item in result:
        if len(item) > 0:
            a = "".join(item)
            answer.append(a)
    print(answer)
    # for query in queries:
    #     if query in cache.values():
    #         result.append(cache)
        
    return answer


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
