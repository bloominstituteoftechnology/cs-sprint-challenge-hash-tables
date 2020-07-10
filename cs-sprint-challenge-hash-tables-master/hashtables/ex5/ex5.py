# Your code here
def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    listed_results = [] # This should become a nested list of possible outputs

    # We are searching for the names that appear in the queries list that also appear in the files list as a part of various file paths.
    # Once we know which file paths contain the query names, we return a list of those file paths.

    for path in files:
        
        # file_item is the substring listed after the last '/'
        file_item = path.split('/')[-1]

        if file_item in cache:
            # If the file_item is already in the cache, then we will append it to the list of values
            cache[file_item].append(path)
        else:
            # if the file_item isn't already in the cache, then we will create a new entry for it
            cache[file_item] = [path]

    for query in queries:

        if query in cache:
            listed_results.append(cache[query])

    # return all of the lists in our nested list into one list
    result = []

    for sublist in listed_results:
        for item in sublist:
            result.append(item)

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