import os

def finder(files, queries):
    hash_table = {}
    result = []

    for path in files:
        filename = os.path.basename(path)
        paths_array = hash_table.get(filename, [])
        paths_array.append(path)
        hash_table[filename] = paths_array
    
    for filename in queries:
        if filename in hash_table:
            result.extend(hash_table[filename])

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
