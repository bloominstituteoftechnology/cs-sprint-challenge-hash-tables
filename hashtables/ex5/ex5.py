# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    copy = files
    table = {}
    end_path = []
    result = []

    for f in copy:
        string = ''
        while f[-1] != '/':
            string += f[-1]
            f = f[:-1]
        string = string[::-1]
        end_path.append(string)

    for i in range(len(files)):
        if end_path[i] not in table:
            table[end_path[i]] = []
        table[end_path[i]].append(files[i])

    for q in queries:
        if q in table:
            r = table.get(q)
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
