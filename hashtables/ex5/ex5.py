import re

def finder(files, queries):
    ht = {}
    for path in files:
        name = re.search(r"/([^/]+)$", path).group(1)
        if name in ht:
            ht[name].append(path)
        else:
            ht[name] = [path]

    result = []
    for q in queries:
        if q in ht:
            for path in ht[q]:
                result.append(path)

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
