# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    z = {}

    for f in files:
        x = f.split("/")
        y = x[-1]

        if y not in z:
            z[y] = []

        z[y].append(f)

    for query in queries:
        if query in z:
            result.extend(z[query])

    return result

"""
line 15: filename is last part of the path
line 17: creates a new entry in the dictionary
line 21: adds current path to dictionary with the filename as the key 
line 24: go through each query
line 27: if the file was found, add all the paths to the results to return
"""


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
