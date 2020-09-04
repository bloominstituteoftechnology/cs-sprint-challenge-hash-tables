# Your code here




cache = {}
def finder(P, Q):
    results = []
    for i in Q:
        cache[i] = i
        #cache[i.split('/')[-1]] = i
        
    for file in P:
        item = file.split('/')[-1]
        if item in cache:
            results.append(file)


    return results

files = [
            '/bin/foo',
            '/bin/bar',
            '/usr/bin/baz'
        ]
queries = [
        "qux"
    ]
print(finder(files, queries))

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
