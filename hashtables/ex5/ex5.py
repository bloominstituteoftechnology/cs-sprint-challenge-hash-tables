# Your code here



def finder(files, queries):
    
    cache = {}
    result = []
    
    for path in files:
        item = path.split('/'[-1])
        
    #     if item in cache:
    #         cache[item].append(path)
    #     else:
    #         cache[item] = [path]
            
    # for query in queries:
    #     if query in cache:
    #         results = cache[query]
    #         for path in results:
    #             result.append(path)

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
