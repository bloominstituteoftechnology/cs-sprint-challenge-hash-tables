# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    listed_results = [] 
    for path in files:
        
        
        file_item = path.split('/')[-1]

        
        if file_item in cache:
            
            cache[file_item].append(path)
        else:
           
            cache[file_item] = [path]


    for query in queries:

        if query in cache:
            listed_results.append(cache[query])

    
    results = []

    for sublist in listed_results:
        for item in sublist:
            results.append(item)

    return results

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
