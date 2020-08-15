# Your code here


def finder(files, queries):
    q_d = {}
    result = []
    for i in queries:
        q_d[i] = 0
    for i in files:
        a = i.split('/')
        if a[len(a)-1] in q_d:
            result.append(i)
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
