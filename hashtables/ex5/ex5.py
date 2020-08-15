# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    file_cache = {}
    query_cache = {}
    result = []

    for file in files:
        file_split = file.split('/')
        file_name = file_split[-1]
        # print(f' file_name: {file_name} in file: {file}')
        if file_name not in file_cache:
            file_cache[file_name] = []   # build list at key
        file_cache[file_name].append(file)    

    # print(file_cache)

    for query in queries:
        if query not in query_cache:
            query_cache[query] = query

    # print(f' \t query_cache {query_cache} ')

    for query in query_cache:
        if query in file_cache:
            # print(f' CACHE HIT on query {query} ')
            # result.append(file_cache[query]) # NOPE add list inside of list (e.g. obj <-> list gets appended)
            # print(f' result {result}')
            result.extend(file_cache[query])   # adds directly to list as args in list iterated 

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



paths = ['/dir256/dirb256/file256',
            '/dir256/file256', '/dir3490/dirb3490/file3490',
            '/dir3490/file3490', '/dir8192/dirb8192/file8192',
            '/dir8192/file8192']


queries = [
    "file3490",
    "file256",
    "file999999",
    "file8192"
]


print(finder(paths, queries))