# Your code here



def finder(files, queries):
    store = {}
    for directory in files:
        dir_splitted = directory.split('/')
        for i in range(len(dir_splitted)):
            if dir_splitted[i] != '':
                if dir_splitted[i] in store:
                    store[dir_splitted[i]] += ['/'.join(dir_splitted[:i+1])]
                else:
                    store[dir_splitted[i]] = ['/'.join(dir_splitted[:i+1])]

    result = []
    for q in queries:
        if q in store:
            result += store[q]

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
