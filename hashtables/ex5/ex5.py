# Your code here



def finder(files, queries):
    file_cache = {}
    query_cache = {}
    result = []
    for file in files:
        split_file = file.split('/')
        file_cache[file] = split_file[-1]
    for query in queries:



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
